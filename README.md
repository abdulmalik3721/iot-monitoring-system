
# IoT Environmental Monitoring System

A Python-based environmental monitoring application that simulates IoT sensor readings, visualizes historical data, and generates automated alerts when configurable thresholds are exceeded.

## 1. Project Overview

The IoT Environmental Monitoring System demonstrates how environmental sensor data can be collected, stored, analyzed, and visualized through a web-based dashboard.

The application generates simulated readings for temperature, humidity, and air quality. It stores the readings in CSV files and provides interactive visualizations, configurable warning and critical thresholds, and an alert-history system.

**Note:** This is a software prototype using simulated sensor data. It does not currently connect to physical sensors or IoT hardware.

## 2. Objectives

- Simulate environmental sensor data.
- Store sensor readings for historical analysis.
- Monitor temperature, humidity, and air-quality index values.
- Visualize sensor readings through interactive charts.
- Configure warning and critical alert thresholds.
- Maintain a timestamped alert history.
- Export sensor readings and alerts as CSV files.

## 3. Key Features

- **Sensor Data Simulation:** Generates simulated temperature, humidity, and air-quality readings.
- **Real-Time Dashboard:** Refreshes the dashboard automatically at regular intervals.
- **Data Persistence:** Stores historical readings in CSV format.
- **Interactive Visualizations:** Displays historical sensor trends using Plotly.
- **Configurable Thresholds:** Allows users to adjust warning and critical limits.
- **Automated Alerts:** Identifies abnormal readings and records warning or critical alerts.
- **Historical Filtering:** Filters readings and alerts by date.
- **CSV Export:** Allows users to download sensor records and alert history.
- **Automated Testing:** Includes unit tests for sensor generation, data storage, and alert management.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic and data processing |
| Streamlit | Interactive web dashboard |
| Pandas | Data handling and analysis |
| Plotly | Interactive data visualization |
| CSV | Sensor and alert data storage |
| unittest | Automated unit testing |
| Git and GitHub | Version control and project hosting |

## 5. Project Structure

```text
iot-monitoring-system/
│
├── app.py
├── sensor_simulator.py
├── alert_manager.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── sensor_data.csv
│   └── alerts.csv
│
├── docs/
│   └── project_report.md
│
├── screenshots/
│
└── tests/
    ├── test_sensor_simulator.py
    └── test_alert_manager.py
```

## 6. System Architecture

The application follows a modular architecture:

1. The sensor simulator generates environmental readings.
2. The application stores readings in a CSV file.
3. The alert manager checks readings against configured thresholds.
4. Generated alerts are stored in a separate CSV file.
5. Streamlit loads the data and displays metrics, charts, and alert history.

## 7. Installation and Setup

### Prerequisites

- Python 3.10 or later recommended.
- Git.
- Visual Studio Code or another Python editor.

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR-GITHUB-USERNAME/iot-monitoring-system.git
```

Replace `YOUR-GITHUB-USERNAME` with your GitHub username.

### Step 2: Navigate to the project

```bash
cd iot-monitoring-system
```

### Step 3: Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

## 8. Running the Application

Start the dashboard using:

```bash
streamlit run app.py
```

Streamlit will provide a local address in the terminal, normally:

```text
http://localhost:8501
```

Open that address in your browser.

## 9. Running Automated Tests

Run the following command from the project root:

```bash
python -m unittest discover -s tests -v
```

The test suite checks:

- Sensor data generation and value ranges.
- Sensor data CSV storage.
- Normal sensor readings without alerts.
- Warning alert generation.
- Critical alert generation.
- Alert CSV storage.

**Current test result:** 6 unit tests passed.

## 10. Data Storage

The project uses two CSV files:

- `data/sensor_data.csv` — stores timestamped sensor readings.
- `data/alerts.csv` — stores generated warning and critical alerts.

These files are created automatically when the application records data or alerts.

## 11. Limitations and Future Improvements

Current limitations:

- Sensor readings are simulated rather than collected from physical hardware.
- The air-quality value is a simulated index, not a certified AQI measurement.
- Data is stored locally in CSV files.
- Alerts are recorded in the dashboard and CSV files; external email or SMS notifications are not implemented.

Possible future improvements:

- Integrate ESP32 or Arduino-based physical sensors.
- Introduce MQTT communication for sensor data transmission.
- Use a relational database for data storage.
- Develop external email or notification services.
- Deploy the dashboard to a cloud platform.
- Add user authentication and access control.

## 12. Project Status

**Status:** Working software prototype with automated unit tests.

The project demonstrates Python programming, modular software development, data handling, visualization, threshold-based monitoring, and automated testing.

## 13. Author

**Abdul Malik**

B.E. Computer Science and Engineering

GitHub: https://github.com/abdulmalik3721
