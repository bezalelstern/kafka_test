from flask import Blueprint, request, jsonify

from stream_consumer.mongo_consumer import get_emails

queries_bp = Blueprint('queries_bp', __name__)


@queries_bp.route('/api/get_sentences', methods=['GET'])
def get_sentences():
    email = request.json.get('email')
    results = get_emails(email)
    sentences = [result['sentence'] for result in results]
    return jsonify(sentences)


