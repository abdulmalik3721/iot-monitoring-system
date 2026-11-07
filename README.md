# iot-monitoring-system
A simulated IoT-based environmental monitoring system using Python, sensor data processing, and a web dashboard

# IoT Monitoring System

## Project Overview

The IoT Monitoring System is a Python-based environmental monitoring application designed to simulate sensor data collection, processing, and visualisation.

The system monitors simulated environmental parameters, including temperature, humidity, and air quality, and presents the readings through an interactive web dashboard.

## Objectives

- Simulate IoT sensor data.
- Collect and process environmental readings.
- Visualise real-time-style sensor measurements.
- Identify abnormal readings using configurable thresholds.
- Provide a simple monitoring dashboard.

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- CSV
- Git and GitHub

## System Architecture

Sensor Simulation → Data Processing → Data Storage → Monitoring Dashboard → Alerts

## Project Structure

```text
iot-monitoring-system/
├── app.py
├── sensor_simulator.py
├── requirements.txt
├── README.md
├── data/
├── docs/
├── screenshots/
└── tests/
```

## Installation

1. Clone the repository.
2. Create a Python virtual environment.
3. Install dependencies using:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
streamlit run app.py
```
