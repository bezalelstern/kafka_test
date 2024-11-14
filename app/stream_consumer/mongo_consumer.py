import json
from kafka import KafkaConsumer
from pymongo import MongoClient

consumer = KafkaConsumer(
     'all_emails',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

mongo_client = MongoClient('mongodb://localhost:27017')
db = mongo_client['email_db']
collection = db['all_emails']

def get_emails(email):
    results = collection.find({'email': email})
    sentences = [result['sentence'] for result in results]
    return sentences


for message in consumer:
    email = message.value
    collection.insert_one(email)
    print(collection.count_documents({}))