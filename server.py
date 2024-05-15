from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv('ES_ENDPOINT'))

app = Flask(__name__)

es = Elasticsearch(
    f"{os.getenv('ES_ENDPOINT')}",
    api_key=f"{os.getenv('API_KEY')}"
)

@app.route('/add_message', methods=['POST'])
def add_message():
    data = request.get_json()
    message = data.get('message')
    print(message)
    res = es.index(index='messages', body={'message': message})
    print(res)
    return jsonify({'message': 'Message added successfully'}), 200

@app.route('/search_message', methods=['GET'])
def search_message():
    keyword = request.args.get('keyword')
    res = es.search(index='messages', body={'query': {'match': {'message': keyword}}})
    print(res)
    hits = res['hits']['hits']
    messages = [hit['_source']['message'] for hit in hits]
    return jsonify({'messages': messages}), 200

if __name__ == '__main__':
    app.run(debug=True)