
import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch

from alert_manager import (
    check_sensor_alerts,
    save_alerts
)


class TestAlertManager(unittest.TestCase):

    def setUp(self):

        self.limits = {
            "temperature": {
                "warning": 30,
                "critical": 35
            },
            "humidity": {
                "warning": 70,
                "critical": 80
            },
            "air_quality": {
                "warning": 150,
                "critical": 180
            }
        }

    def test_no_alert_for_normal_readings(self):

        reading = {
            "timestamp": "2026-11-07 10:00:00",
            "temperature": 25,
            "humidity": 50,
            "air_quality": 100
        }

        alerts = check_sensor_alerts(
            reading,
            self.limits
        )

        self.assertEqual(len(alerts), 0)

    def test_warning_alert(self):

        reading = {
            "timestamp": "2026-11-07 10:00:00",
            "temperature": 32,
            "humidity": 50,
            "air_quality": 100
        }

        alerts = check_sensor_alerts(
            reading,
            self.limits
        )

        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]["severity"], "Warning")
        self.assertEqual(alerts[0]["sensor"], "Temperature")

    def test_critical_alert(self):

        reading = {
            "timestamp": "2026-11-07 10:00:00",
            "temperature": 37,
            "humidity": 50,
            "air_quality": 100
        }

        alerts = check_sensor_alerts(
            reading,
            self.limits
        )

        self.assertEqual(len(alerts), 1)
        self.assertEqual(alerts[0]["severity"], "Critical")

    def test_save_alerts(self):

        alerts = [{
            "timestamp": "2026-11-07 10:00:00",
            "sensor": "Temperature",
            "value": 37,
            "severity": "Critical",
            "message": "Temperature has reached a critical level"
        }]

        with tempfile.TemporaryDirectory() as temp_dir:

            test_file = Path(temp_dir) / "alerts.csv"

            with patch("alert_manager.ALERT_FILE", test_file):

                save_alerts(alerts)

                self.assertTrue(test_file.exists())

                with open(test_file, "r", encoding="utf-8") as file:
                    content = file.read()

                self.assertIn("Critical", content)
                self.assertIn("Temperature", content)


if __name__ == "__main__":
    unittest.main()
