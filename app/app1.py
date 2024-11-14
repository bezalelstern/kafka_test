import json
from kafka import KafkaProducer
from flask import Flask, request, jsonify
# from queries import queries_bp
from stream_consumer.db_postgres.database import init_db

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))
app = Flask(__name__)

# app.register_blueprint(queries_bp)

@app.route('/api/email', methods=[ 'POST'])
def index():
    data = request.json
    producer.send(topic="stream", value= data)
    return 'OK'



if __name__ == '__main__':
    init_db()
    app.run(debug=True)