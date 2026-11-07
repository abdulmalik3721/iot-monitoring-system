
import streamlit as st
import pandas as pd
import plotly.express as px

from pathlib import Path
from streamlit_autorefresh import st_autorefresh

from sensor_simulator import (
    generate_sensor_data,
    save_sensor_data
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

st.markdown(
    "Advanced environmental monitoring dashboard "
    "using simulated IoT sensor readings."
)

DATA_FILE = Path("data/sensor_data.csv")


# ------------------------------------------------
# 2. AUTOMATIC SENSOR DATA COLLECTION
# ------------------------------------------------

st_autorefresh(
    interval=10000,
    key="sensor_refresh"
)

new_reading = generate_sensor_data()
save_sensor_data(new_reading)


# ------------------------------------------------
# 3. LOAD SENSOR DATA
# ------------------------------------------------

df = pd.read_csv(DATA_FILE)

df["timestamp"] = pd.to_datetime(df["timestamp"])

latest = df.iloc[-1]


# ------------------------------------------------
# 4. SIDEBAR CONFIGURATION
# ------------------------------------------------

st.sidebar.header("Dashboard Settings")

temperature_limit = st.sidebar.slider(
    "Temperature threshold (°C)",
    min_value=20,
    max_value=40,
    value=30
)

humidity_limit = st.sidebar.slider(
    "Humidity threshold (%)",
    min_value=40,
    max_value=100,
    value=70
)

air_quality_limit = st.sidebar.slider(
    "Air quality threshold",
    min_value=50,
    max_value=250,
    value=150
)

st.sidebar.caption("Dashboard refreshes every 10 seconds.")


# ------------------------------------------------
# 5. DATE FILTERING
# ------------------------------------------------

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
    (df["timestamp"].dt.date >= start_date) &
    (df["timestamp"].dt.date <= end_date)
].copy()


# ------------------------------------------------
# 6. SENSOR METRICS
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
    "Air Quality",
    f"{latest['air_quality']}"
)

col4.metric(
    "Total Readings",
    len(df)
)


# ------------------------------------------------
# 7. SENSOR STATUS
# ------------------------------------------------

st.subheader("Sensor Status")

status1, status2, status3 = st.columns(3)

with status1:

    if latest["temperature"] > temperature_limit:
        st.error("High Temperature")
    else:
        st.success("Temperature Normal")

with status2:

    if latest["humidity"] > humidity_limit:
        st.error("High Humidity")
    else:
        st.success("Humidity Normal")

with status3:

    if latest["air_quality"] > air_quality_limit:
        st.error("Poor Air Quality")
    else:
        st.success("Air Quality Normal")


# ------------------------------------------------
# 8. HISTORICAL DATA VISUALIZATION
# ------------------------------------------------

st.subheader("Historical Sensor Analytics")

if filtered_df.empty:

    st.warning("No readings available for this date range.")

else:

    # Temperature chart
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

    # Humidity chart
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

    # Air quality chart
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
# 9. DOWNLOAD SENSOR DATA
# ------------------------------------------------

st.subheader("Export Sensor Data")

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Sensor Data (CSV)",
    data=csv_data,
    file_name="iot_sensor_data.csv",
    mime="text/csv"
)


# ------------------------------------------------
# 10. HISTORICAL SENSOR TABLE
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
# 11. PROJECT INFORMATION
# ------------------------------------------------

st.divider()

st.caption(
    "IoT Monitoring System | Python | Streamlit | "
    "Pandas | Plotly"
)

st.caption(
    "Note: All readings are simulated. "
    "No physical sensors are connected."
)
