import json

from kafka import KafkaConsumer, KafkaProducer

consumer = KafkaConsumer(
    'stream',
    group_id='email_group',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def chek_explosive(email):
    sentences = email["sentences"]
    if "explos" in sentences:
        return True

def chek_hostage(email):
    sentences = email["sentences"]
    if "hostage" in sentences:
        return True



all_messages = KafkaProducer(bootstrap_servers=['localhost:9092'],
                               value_serializer=lambda v: json.dumps(v).encode('utf-8'))
hostage_messages = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                    value_serializer=lambda v: json.dumps(v).encode('utf-8'))
explosive_messages = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                               value_serializer=lambda v: json.dumps(v).encode('utf-8'))


for message in consumer:
    email = message.value
    all_messages.send(topic="all_emails", value=email)
    if chek_explosive(email):
        explosive_messages.send(topic="explosive_emails", value=email)
    if chek_hostage(email):
        hostage_messages.send(topic='hostages_emails', value=email)



