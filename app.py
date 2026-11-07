
import streamlit as st
import pandas as pd
import plotly.express as px

from pathlib import Path
from streamlit_autorefresh import st_autorefresh

from sensor_simulator import (
    generate_sensor_data,
    save_sensor_data
)


# Dashboard configuration
st.set_page_config(
    page_title="IoT Monitoring System",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 IoT Environmental Monitoring System")

st.write(
    "Automated environmental monitoring using "
    "simulated IoT sensor readings."
)

DATA_FILE = Path("data/sensor_data.csv")

# Automatically refresh every 10 seconds
refresh_count = st_autorefresh(
    interval=10000,
    key="sensor_refresh"
)

# Generate and save a new reading on each refresh
new_reading = generate_sensor_data()
save_sensor_data(new_reading)

# Read historical sensor data
df = pd.read_csv(DATA_FILE)

# Convert timestamp into datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Latest readings
latest = df.iloc[-1]

st.caption("Dashboard automatically updates every 10 seconds.")

# Display metrics
col1, col2, col3 = st.columns(3)

col1.metric(
    "Temperature",
    f"{latest['temperature']} °C"
)

col2.metric(
    "Humidity",
    f"{latest['humidity']} %"
)

col3.metric(
    "Air Quality",
    f"{latest['air_quality']}"
)

st.divider()

# Temperature graph
st.subheader("Temperature Monitoring")

temperature_chart = px.line(
    df,
    x="timestamp",
    y="temperature",
    title="Temperature History",
    markers=True
)

st.plotly_chart(
    temperature_chart,
    use_container_width=True
)

# Humidity graph
st.subheader("Humidity Monitoring")

humidity_chart = px.line(
    df,
    x="timestamp",
    y="humidity",
    title="Humidity History",
    markers=True
)

st.plotly_chart(
    humidity_chart,
    use_container_width=True
)

# Air quality graph
st.subheader("Air Quality Monitoring")

air_chart = px.line(
    df,
    x="timestamp",
    y="air_quality",
    title="Air Quality History",
    markers=True
)

st.plotly_chart(
    air_chart,
    use_container_width=True
)

st.divider()

# Monitoring alerts
st.subheader("Monitoring Alerts")

if latest["temperature"] > 30:
    st.warning("High temperature detected!")
else:
    st.success("Temperature is within the configured threshold.")

if latest["humidity"] > 70:
    st.warning("High humidity detected!")
else:
    st.success("Humidity is within the configured threshold.")

# Historical data
st.subheader("Historical Sensor Readings")

st.dataframe(
    df.sort_values("timestamp", ascending=False),
    use_container_width=True
)

st.write(f"Total sensor readings: {len(df)}")

st.caption(
    "All sensor readings are simulated. "
    "No physical IoT hardware is connected."
)
