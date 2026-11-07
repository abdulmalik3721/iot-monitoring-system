
# Technical Project Report
## IoT Environmental Monitoring System

### 1. Introduction

The IoT Environmental Monitoring System is a Python-based software prototype designed to demonstrate environmental data monitoring and analysis. It simulates sensor readings for temperature, humidity, and air quality and presents the information through an interactive web dashboard.

### 2. Problem Statement

Environmental monitoring involves observing changing environmental conditions and identifying readings that exceed predefined limits. This project demonstrates a software approach to collecting, recording, visualizing, and monitoring such readings.

### 3. Project Objectives

- Generate simulated environmental sensor readings.
- Store readings for historical analysis.
- Display environmental data through an interactive dashboard.
- Identify abnormal readings using configurable thresholds.
- Maintain a timestamped record of alerts.
- Support historical data filtering and CSV export.

### 4. System Design

The system is divided into three main software modules.

**Sensor Simulator**

The `sensor_simulator.py` module generates simulated temperature, humidity, and air-quality readings. It also stores the generated readings in a CSV file.

**Alert Manager**

The `alert_manager.py` module compares sensor readings against configurable warning and critical thresholds. It generates alerts and stores them in a separate CSV file.

**Dashboard Application**

The `app.py` module uses Streamlit to display sensor metrics, historical charts, sensor status, alert summaries, and downloadable records.

### 5. Data Management

The application uses CSV files for local data persistence.

- `sensor_data.csv`: Stores environmental sensor readings.
- `alerts.csv`: Stores warning and critical alert records.

### 6. Testing and Validation

The project includes automated unit tests using Python's built-in `unittest` framework.

Six tests were executed successfully, covering:

- Sensor data generation.
- Sensor data storage.
- Normal readings.
- Warning alert generation.
- Critical alert generation.
- Alert storage.

**Test result: 6 tests passed.**

### 7. Technologies

- Python
- Streamlit
- Pandas
- Plotly
- CSV
- unittest
- Git and GitHub

### 8. Limitations

The current implementation uses simulated sensor data and does not communicate with physical IoT hardware. The air-quality value is a simulated index and is not a certified air-quality measurement. Data is stored locally in CSV files.

### 9. Future Scope

Future development could include physical sensor integration using ESP32 or Arduino, MQTT-based communication, database integration, cloud deployment, and external alert notifications.

### 10. Conclusion

The project demonstrates a modular software prototype for environmental monitoring. It combines data generation, persistence, visualization, threshold-based alerting, and automated testing in a single application.
