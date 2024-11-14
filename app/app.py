import json
from kafka import KafkaProducer
from flask import Flask, request

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))
app = Flask(__name__)
@app.route('/api/email', methods=[ 'POST'])
def index():
    data = request.json
    producer.send(topic="stream", value= data)
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)