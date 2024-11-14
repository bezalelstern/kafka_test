import json
from kafka import KafkaConsumer
from pymongo import MongoClient

consumer = KafkaConsumer(
     'hostages_emails',
    bootstrap_servers='localhost:9092',
    group_id='hostage_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for msg in consumer:
    email = msg.value
    print(email)