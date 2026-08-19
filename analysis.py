import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Load the CSV data
df = pd.read_csv("Sample_Data.csv")

# Convert Timestamp column to datetime
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Display first few rows
print(df.head())

# Plot Voltage vs Timestamp
plt.figure(figsize=(12, 6))
df["Moving_Average_5D"] = df.rolling("5D", on="Timestamp")["Values"].mean().values
plt.plot(df["Timestamp"], df["Values"], label="Voltage")
plt.plot(df["Timestamp"], df["Moving_Average_5D"], label="5-Day Moving Average")

plt.xlabel("Timestamp")
plt.ylabel("Voltage")
plt.title("Voltage vs Timestamp")
plt.legend()
plt.grid(True)
# Find local peaks and lows
peaks, _ = find_peaks(df["Values"])
lows, _ = find_peaks(-df["Values"])

# Create tables
peak_table = df.iloc[peaks][["Timestamp", "Values"]]
low_table = df.iloc[lows][["Timestamp", "Values"]]

print("\nLOCAL PEAKS:")
print(peak_table.to_string(index=False))

print("\nLOCAL LOWS:")
print(low_table.to_string(index=False))
# Find all instances where voltage is below 20
below_20 = df[df["Values"] < 20][["Timestamp", "Values"]]

print("\nVOLTAGE BELOW 20:")
print(below_20.to_string(index=False))
# Bonus: Find where the downward slope accelerates

time_diff = df["Timestamp"].diff().dt.total_seconds()
df["Slope"] = df["Values"].diff() / time_diff.replace(0, float("nan"))

# Acceleration of downward slope
df["Slope_Change"] = df["Slope"].diff()

# Downward slope is accelerating when slope becomes more negative
accelerating_down = df[
    (df["Slope"] < 0) &
    (df["Slope_Change"] < 0)
]

print("\nDOWNWARD SLOPE ACCELERATION:")
print(accelerating_down[["Timestamp", "Values", "Slope"]].to_string(index=False))
plt.show()