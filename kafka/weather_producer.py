
import json
import time
import random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]

while True:
    city = random.choice(cities)
    weather_data = {
        "city": city,
        "temperature": round(random.uniform(15, 35), 2),
        "humidity": random.randint(40, 90),
        "description": random.choice(["Clear", "Rain", "Cloudy", "Storm"]),
    }

    print(f"Sending weather data: {weather_data}")
    producer.send('weather', weather_data)
    time.sleep(3)
