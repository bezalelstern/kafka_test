import json
from kafka import KafkaConsumer

from ..db_postgres.database import db_session
from ..db_postgres.models import ExplosiveModel
consumer = KafkaConsumer(
     'explosive_emails',
    bootstrap_servers='localhost:9092',
    group_id='hostage_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for msg in consumer:
    email = msg.value
    print(email['sentences'][0])
    model = ExplosiveModel(email['sentences'])
    db_session.add(model)
    db_session.commit()
