import json
from kafka import KafkaConsumer, KafkaProducer

from service import chek_explosive, chek_hostage

consumer = KafkaConsumer(
    'stream',
    group_id='email_group',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)



producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))


for message in consumer:
    email = message.value
    producer.send(topic="all_emails", value=email)

    explosive, email["sentences"] = chek_explosive(email)
    hostages, email["sentences"] = chek_hostage(email)

    if explosive:
         producer.send(topic="explosive_emails", value=email)
    if hostages:
        producer.send(topic='hostages_emails', value=email)



