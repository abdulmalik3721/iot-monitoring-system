
import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch

from sensor_simulator import (
    generate_sensor_data,
    save_sensor_data
)


class TestSensorSimulator(unittest.TestCase):

    def test_generate_sensor_data(self):

        reading = generate_sensor_data()

        # Check required fields
        self.assertIn("timestamp", reading)
        self.assertIn("temperature", reading)
        self.assertIn("humidity", reading)
        self.assertIn("air_quality", reading)

        # Check generated values are within expected ranges
        self.assertGreaterEqual(reading["temperature"], 20)
        self.assertLessEqual(reading["temperature"], 35)

        self.assertGreaterEqual(reading["humidity"], 30)
        self.assertLessEqual(reading["humidity"], 80)

        self.assertGreaterEqual(reading["air_quality"], 50)
        self.assertLessEqual(reading["air_quality"], 200)

    def test_save_sensor_data(self):

        reading = generate_sensor_data()

        with tempfile.TemporaryDirectory() as temp_dir:

            test_file = Path(temp_dir) / "sensor_data.csv"

            with patch("sensor_simulator.DATA_FILE", test_file):

                save_sensor_data(reading)

                self.assertTrue(test_file.exists())

                with open(test_file, "r", encoding="utf-8") as file:
                    content = file.read()

                self.assertIn("temperature", content)
                self.assertIn(str(reading["temperature"]), content)


if __name__ == "__main__":
    unittest.main()
