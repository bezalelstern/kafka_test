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
        print("subolo")
        return True


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))


all_messages = KafkaProducer(bootstrap_servers=['localhost:9092'],
                               value_serializer=lambda v: json.dumps(v).encode('utf-8'))
hostage_messages = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                    value_serializer=lambda v: json.dumps(v).encode('utf-8'))
explosive_messages = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                               value_serializer=lambda v: json.dumps(v).encode('utf-8'))


for message in consumer:
    email = message.value
    print(email)
    producer.send(topic="all_emails", value=email)
    # if chek_explosive(email):
    #     producer.send(topic="explosive_emails", value=email)
    # if chek_hostage(email):
    producer.send(topic='hostages_emails', value=email)



