# GreenCell Voltage Analysis

A Python-based data analysis application for analyzing GreenCell voltage data using Pandas and Matplotlib, with a Flask web interface for displaying dataset insights.

## Features

- Load and analyze GreenCell voltage data
- Convert timestamps into datetime format
- Calculate minimum, maximum, and average voltage
- Calculate a 5-day moving average
- Identify local voltage peaks and lows
- Find instances where voltage is below 20
- Detect instances where downward voltage slope accelerates
- Visualize voltage trends using Matplotlib
- Deploy the Flask application as a live web service

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- SciPy
- Flask
- Gunicorn

## Project Files

- `analysis.py` – Data analysis, moving average, peaks/lows and slope analysis
- `app.py` – Flask web application
- `requirements.txt` – Python dependencies
- `Sample_Data.csv` – Input dataset
- `Sample_Data.xlsx` – Excel version of the dataset

## Dataset Summary

- Total records: 21,919
- Minimum voltage: 25
- Maximum voltage: 100
- Average voltage: 67.33
- Voltage below 20: 0 records

## Run Locally

```bash
pip install -r requirements.txt
python analysis.py
