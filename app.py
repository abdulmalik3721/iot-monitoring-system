
import streamlit as st
import pandas as pd
import plotly.express as px

from pathlib import Path
from streamlit_autorefresh import st_autorefresh

from sensor_simulator import (
    generate_sensor_data,
    save_sensor_data
)

from alert_manager import (
    check_sensor_alerts,
    save_alerts
)


# ------------------------------------------------
# 1. PAGE CONFIGURATION
# ------------------------------------------------

st.set_page_config(
    page_title="IoT Monitoring System",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 IoT Environmental Monitoring System")

st.write(
    "Environmental monitoring dashboard using simulated "
    "IoT sensor readings and automated alerts."
)

DATA_FILE = Path("data/sensor_data.csv")
ALERT_FILE = Path("data/alerts.csv")


# ------------------------------------------------
# 2. SIDEBAR: ALERT THRESHOLDS
# ------------------------------------------------

st.sidebar.header("Alert Configuration")

st.sidebar.subheader("Temperature")

temp_warning = st.sidebar.slider(
    "Temperature warning limit (°C)",
    min_value=20,
    max_value=35,
    value=30
)

temp_critical = st.sidebar.slider(
    "Temperature critical limit (°C)",
    min_value=temp_warning + 1,
    max_value=40,
    value=min(temp_warning + 3, 40)
)

st.sidebar.subheader("Humidity")

humidity_warning = st.sidebar.slider(
    "Humidity warning limit (%)",
    min_value=40,
    max_value=90,
    value=70
)

humidity_critical = st.sidebar.slider(
    "Humidity critical limit (%)",
    min_value=humidity_warning + 1,
    max_value=100,
    value=min(humidity_warning + 10, 100)
)

st.sidebar.subheader("Air Quality")

air_warning = st.sidebar.slider(
    "Air quality warning limit",
    min_value=50,
    max_value=220,
    value=150
)

air_critical = st.sidebar.slider(
    "Air quality critical limit",
    min_value=air_warning + 1,
    max_value=250,
    value=min(air_warning + 30, 250)
)

limits = {
    "temperature": {
        "warning": temp_warning,
        "critical": temp_critical
    },
    "humidity": {
        "warning": humidity_warning,
        "critical": humidity_critical
    },
    "air_quality": {
        "warning": air_warning,
        "critical": air_critical
    }
}


# ------------------------------------------------
# 3. AUTOMATIC SENSOR DATA COLLECTION
# ------------------------------------------------

refresh_count = st_autorefresh(
    interval=10000,
    key="sensor_refresh"
)

# Collect a reading only on the first run or when
# the automatic refresh counter changes.
should_collect = (
    "last_refresh_count" not in st.session_state
    or st.session_state.last_refresh_count != refresh_count
)

if should_collect:

    new_reading = generate_sensor_data()
    save_sensor_data(new_reading)

    new_alerts = check_sensor_alerts(
        new_reading,
        limits
    )

    save_alerts(new_alerts)

    st.session_state.last_refresh_count = refresh_count


# ------------------------------------------------
# 4. LOAD SENSOR DATA
# ------------------------------------------------

if not DATA_FILE.exists():
    st.error("Sensor data file was not created.")
    st.stop()

df = pd.read_csv(DATA_FILE)

if df.empty:
    st.warning("No sensor readings are available yet.")
    st.stop()

df["timestamp"] = pd.to_datetime(df["timestamp"])

latest = df.iloc[-1]


# ------------------------------------------------
# 5. LOAD ALERT HISTORY
# ------------------------------------------------

alert_columns = [
    "timestamp",
    "sensor",
    "value",
    "severity",
    "message"
]

if ALERT_FILE.exists():

    alerts_df = pd.read_csv(ALERT_FILE)

else:

    alerts_df = pd.DataFrame(columns=alert_columns)

if not alerts_df.empty:
    alerts_df["timestamp"] = pd.to_datetime(
        alerts_df["timestamp"]
    )


# ------------------------------------------------
# 6. DATE FILTERS
# ------------------------------------------------

st.sidebar.divider()
st.sidebar.subheader("Historical Data Filter")

start_date = st.sidebar.date_input(
    "Start date",
    value=df["timestamp"].min().date()
)

end_date = st.sidebar.date_input(
    "End date",
    value=df["timestamp"].max().date()
)

if start_date > end_date:
    st.error("Start date cannot be after end date.")
    st.stop()

filtered_df = df[
    (df["timestamp"].dt.date >= start_date)
    & (df["timestamp"].dt.date <= end_date)
].copy()

if not alerts_df.empty:

    filtered_alerts = alerts_df[
        (alerts_df["timestamp"].dt.date >= start_date)
        & (alerts_df["timestamp"].dt.date <= end_date)
    ].copy()

else:

    filtered_alerts = alerts_df.copy()


# ------------------------------------------------
# 7. CURRENT SENSOR READINGS
# ------------------------------------------------

st.subheader("Current Sensor Readings")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Temperature",
    f"{latest['temperature']} °C"
)

col2.metric(
    "Humidity",
    f"{latest['humidity']} %"
)

col3.metric(
    "Air Quality Index",
    f"{latest['air_quality']}"
)

col4.metric(
    "Total Readings",
    len(df)
)

st.caption("Dashboard automatically refreshes every 10 seconds.")


# ------------------------------------------------
# 8. CURRENT SENSOR STATUS
# ------------------------------------------------

st.subheader("Sensor Status")

status1, status2, status3 = st.columns(3)

sensor_values = {
    "temperature": latest["temperature"],
    "humidity": latest["humidity"],
    "air_quality": latest["air_quality"]
}

with status1:

    value = sensor_values["temperature"]

    if value >= temp_critical:
        st.error("Temperature: Critical")
    elif value >= temp_warning:
        st.warning("Temperature: Warning")
    else:
        st.success("Temperature: Normal")

with status2:

    value = sensor_values["humidity"]

    if value >= humidity_critical:
        st.error("Humidity: Critical")
    elif value >= humidity_warning:
        st.warning("Humidity: Warning")
    else:
        st.success("Humidity: Normal")

with status3:

    value = sensor_values["air_quality"]

    if value >= air_critical:
        st.error("Air Quality: Critical")
    elif value >= air_warning:
        st.warning("Air Quality: Warning")
    else:
        st.success("Air Quality: Normal")


# ------------------------------------------------
# 9. HISTORICAL SENSOR CHARTS
# ------------------------------------------------

st.subheader("Historical Sensor Analytics")

if filtered_df.empty:

    st.warning("No readings available for this date range.")

else:

    temperature_chart = px.line(
        filtered_df,
        x="timestamp",
        y="temperature",
        title="Temperature History",
        markers=True
    )

    st.plotly_chart(
        temperature_chart,
        use_container_width=True
    )

    humidity_chart = px.line(
        filtered_df,
        x="timestamp",
        y="humidity",
        title="Humidity History",
        markers=True
    )

    st.plotly_chart(
        humidity_chart,
        use_container_width=True
    )

    air_chart = px.line(
        filtered_df,
        x="timestamp",
        y="air_quality",
        title="Air Quality History",
        markers=True
    )

    st.plotly_chart(
        air_chart,
        use_container_width=True
    )


# ------------------------------------------------
# 10. ALERT SUMMARY
# ------------------------------------------------

st.divider()
st.subheader("🚨 Automated Alert Summary")

if filtered_alerts.empty:

    st.success("No alerts recorded for the selected date range.")

else:

    warning_count = (
        filtered_alerts["severity"] == "Warning"
    ).sum()

    critical_count = (
        filtered_alerts["severity"] == "Critical"
    ).sum()

    alert_col1, alert_col2 = st.columns(2)

    alert_col1.metric(
        "Warning Alerts",
        int(warning_count)
    )

    alert_col2.metric(
        "Critical Alerts",
        int(critical_count)
    )


# ------------------------------------------------
# 11. ALERT HISTORY
# ------------------------------------------------

st.subheader("Alert History")

if filtered_alerts.empty:

    st.info("Alert history is currently empty.")

else:

    st.dataframe(
        filtered_alerts.sort_values(
            "timestamp",
            ascending=False
        ),
        use_container_width=True
    )

    alert_csv = filtered_alerts.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="Download Alert History (CSV)",
        data=alert_csv,
        file_name="iot_alert_history.csv",
        mime="text/csv"
    )


# ------------------------------------------------
# 12. SENSOR DATA EXPORT
# ------------------------------------------------

st.divider()
st.subheader("Export Sensor Data")

csv_data = filtered_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Sensor Data (CSV)",
    data=csv_data,
    file_name="iot_sensor_data.csv",
    mime="text/csv"
)


# ------------------------------------------------
# 13. SENSOR RECORDS
# ------------------------------------------------

st.subheader("Sensor Reading Records")

st.dataframe(
    filtered_df.sort_values(
        "timestamp",
        ascending=False
    ),
    use_container_width=True
)


# ------------------------------------------------
# 14. PROJECT INFORMATION
# ------------------------------------------------

st.divider()

st.caption(
    "IoT Monitoring System | Python | Streamlit | "
    "Pandas | Plotly | Automated Alert Logging"
)

st.caption(
    "All sensor readings are simulated. "
    "No physical sensors are connected. "
    "Air quality is represented by a simulated index, "
    "not a certified AQI measurement."
)
