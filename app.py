from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    df = pd.read_csv("Sample_Data.csv")
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])

    return render_template_string("""
    <html>
    <head>
        <title>GreenCell Voltage Analysis</title>
    </head>
    <body>
        <h1>GreenCell Voltage Analysis</h1>
        <p>Python data analysis application</p>

        <h2>Dataset Summary</h2>
        <p>Total records: {{ total }}</p>
        <p>Minimum voltage: {{ minimum }}</p>
        <p>Maximum voltage: {{ maximum }}</p>
        <p>Average voltage: {{ average }}</p>

        <h2>Voltage Below 20</h2>
        <p>{{ below20 }} records found.</p>
    </body>
    </html>
    """,
    total=len(df),
    minimum=df["Values"].min(),
    maximum=df["Values"].max(),
    average=round(df["Values"].mean(), 2),
    below20=len(df[df["Values"] < 20])
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)