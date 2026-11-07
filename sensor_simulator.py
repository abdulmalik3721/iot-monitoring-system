
import random
import csv
from pathlib import Path
from datetime import datetime


# Location of CSV file
DATA_FILE = Path("data/sensor_data.csv")


def generate_sensor_data():

    data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(30, 80), 2),
        "air_quality": round(random.uniform(50, 200), 2)
    }

    return data


def save_sensor_data(data):

    # Create data folder if it doesn't exist
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    file_exists = DATA_FILE.exists()

    with open(DATA_FILE, "a", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "timestamp",
                "temperature",
                "humidity",
                "air_quality"
            ]
        )

        # Write column headings for a new file
        if not file_exists or DATA_FILE.stat().st_size == 0:
            writer.writeheader()

        writer.writerow(data)

    print("Sensor data saved successfully!")


if __name__ == "__main__":

    sensor_data = generate_sensor_data()

    print(sensor_data)

    save_sensor_data(sensor_data)
