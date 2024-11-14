import json
from kafka import KafkaConsumer
from pymongo import MongoClient

consumer = KafkaConsumer(
     'all_emails',
    bootstrap_servers='localhost:9092',
    # group_id='email_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

mongo_client = MongoClient('mongodb://localhost:27017')
db = mongo_client['email_db']
high_value_collection = db['all_emails']


for message in consumer:
    email = message.value
    high_value_collection.insert_one(email)
    print(high_value_collection.count_documents({}))