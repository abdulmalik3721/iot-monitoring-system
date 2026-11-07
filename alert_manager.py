
import csv
from pathlib import Path
from datetime import datetime


ALERT_FILE = Path("data/alerts.csv")

ALERT_FIELDS = [
    "timestamp",
    "sensor",
    "value",
    "severity",
    "message"
]


def check_sensor_alerts(reading, limits):
    """Check a sensor reading and return any alerts."""

    alerts = []

    sensors = {
        "temperature": "Temperature",
        "humidity": "Humidity",
        "air_quality": "Air Quality"
    }

    for key, sensor_name in sensors.items():

        value = reading[key]
        warning_limit = limits[key]["warning"]
        critical_limit = limits[key]["critical"]

        if value >= critical_limit:
            severity = "Critical"
            message = (
                f"{sensor_name} has reached a critical level: {value}"
            )

        elif value >= warning_limit:
            severity = "Warning"
            message = (
                f"{sensor_name} has crossed the warning limit: {value}"
            )

        else:
            continue

        alerts.append({
            "timestamp": reading["timestamp"],
            "sensor": sensor_name,
            "value": value,
            "severity": severity,
            "message": message
        })

    return alerts


def save_alerts(alerts):
    """Append generated alerts to the alert history CSV file."""

    if not alerts:
        return

    ALERT_FILE.parent.mkdir(parents=True, exist_ok=True)

    file_exists = ALERT_FILE.exists()

    with open(ALERT_FILE, "a", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=ALERT_FIELDS
        )

        if not file_exists or ALERT_FILE.stat().st_size == 0:
            writer.writeheader()

        writer.writerows(alerts)
