
import streamlit as st
import pandas as pd
import plotly.express as px

from pathlib import Path
from sensor_simulator import (
    generate_sensor_data,
    save_sensor_data
)


st.set_page_config(
    page_title="IoT Monitoring System",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 IoT Environmental Monitoring System")

st.write(
    "Environmental monitoring using simulated "
    "IoT sensor readings."
)

DATA_FILE = Path("data/sensor_data.csv")


# Collect a new sensor reading
if st.button("Collect New Sensor Reading"):

    new_reading = generate_sensor_data()

    save_sensor_data(new_reading)

    st.success("New sensor reading collected and saved!")


# Load saved readings
if DATA_FILE.exists() and DATA_FILE.stat().st_size > 0:

    df = pd.read_csv(DATA_FILE)

else:

    df = pd.DataFrame(columns=[
        "timestamp",
        "temperature",
        "humidity",
        "air_quality"
    ])


if df.empty:

    st.info("No sensor readings available. Collect a reading to begin.")

else:

    latest = df.iloc[-1]

    # Current sensor measurements
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

    # Temperature chart
    st.subheader("Temperature Monitoring")

    temperature_chart = px.line(
        df,
        x="timestamp",
        y="temperature",
        title="Temperature History"
    )

    st.plotly_chart(
        temperature_chart,
        use_container_width=True
    )

    # Humidity chart
    st.subheader("Humidity Monitoring")

    humidity_chart = px.line(
        df,
        x="timestamp",
        y="humidity",
        title="Humidity History"
    )

    st.plotly_chart(
        humidity_chart,
        use_container_width=True
    )

    # Air quality chart
    st.subheader("Air Quality Monitoring")

    air_chart = px.line(
        df,
        x="timestamp",
        y="air_quality",
        title="Air Quality History"
    )

    st.plotly_chart(
        air_chart,
        use_container_width=True
    )

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

    # Historical records
    st.subheader("Historical Sensor Readings")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.write(f"Total sensor readings: {len(df)}")


st.caption("Sensor readings are simulated for demonstration purposes.")
