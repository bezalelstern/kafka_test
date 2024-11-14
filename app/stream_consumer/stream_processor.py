import json
from imaplib import Flags

from kafka import KafkaConsumer, KafkaProducer

from app.app import index

consumer = KafkaConsumer(
    'stream',
    group_id='email_group',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def chek_explosive(email):
    sentences = email["sentences"]
    index = -1
    flag = False
    sherch_word = "explos"
    for sentence in sentences:
        if sherch_word in sentence.lower():
            index = sentences.index(sentence)
            flag =  True
            break
    if flag:
        sentence = sentences[index]
        sentences.pop(index)
        sentences.insert(0, sentence)

    return flag, sentences


def chek_hostage(email):
    sentences = email["sentences"]
    index = -1
    flag = False
    sherch_word = "hotage"
    for sentence in sentences:
        if sherch_word in sentence.lower():
            index = sentences.index(sentence)
            flag =  True
            break
    if flag:
        sentence = sentences[index]
        sentences.pop(index)
        sentences.insert(0, sentence)

    return flag, sentences


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))


for message in consumer:
    email = message.value
    producer.send(topic="all_emails", value=email)

    explosive, email["sentences"] = chek_explosive(email)
    hostages, email["sentences"] = chek_explosive(email)

    if explosive:
         producer.send(topic="explosive_emails", value=email)
    if hostages:
        producer.send(topic='hostages_emails', value=email)



