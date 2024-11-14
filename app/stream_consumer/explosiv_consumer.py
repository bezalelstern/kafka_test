import json
from kafka import KafkaConsumer
from sqlalchemy.orm import Session

from db_postgres.database import db_session
from db_postgres.models import ExplosiveModel, EmailModel

consumer = KafkaConsumer(
     'explosive_emails',
    bootstrap_servers='localhost:9092',
    group_id='hostage_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)



for msg in consumer:
    email = msg.value
    print(email['sentences'][0])
    string_email = str(email['sentences'])

    try:
        model = ExplosiveModel(content=string_email)
        db_email = EmailModel(email=email["email"],username=email["username"])
        db_email.explosive_contents.append(model)
        db_session.add(db_email)
        db_session.commit()

    except Exception as e:
        db_session.rollback()
        print(e)