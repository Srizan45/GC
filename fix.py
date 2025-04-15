from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
print("Kafka Producer Connected ✅")
