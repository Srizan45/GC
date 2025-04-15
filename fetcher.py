import json
import time
from kafka import KafkaProducer
import undetected_chromedriver as uc

def fetch_sofascore_data():
    url = "https://www.sofascore.com/api/v1/sport/football/events/live"
    options = uc.ChromeOptions()
    options.add_argument("--headless")
    driver = uc.Chrome(options=options)

    driver.get("https://www.sofascore.com/")
    driver.execute_script(f'''
        window._data = null;
        fetch("{url}")
            .then(response => response.json())
            .then(data => window._data = data)
    ''')

    for _ in range(20):  # wait max 10s
        data = driver.execute_script("return window._data")
        if data: break
        time.sleep(0.5)

    driver.quit()
    return data or {}

# Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = fetch_sofascore_data()
    print("🔄 Sending to Kafka:", data.get("events", [])[:1])  # preview
    producer.send("live-sports", value=data)
    time.sleep(15)
