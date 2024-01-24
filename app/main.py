from flask import Flask, jsonify, request
import requests

from app.handlers.post_handler import handle

app = Flask(__name__)

# Replace this URL with the URL of your Fuseki server and dataset
fuseki_endpoint = "http://localhost:3030/ds/query"


@app.route('/conversion', methods=['POST'])
def post():
    data = request.get_json()
    return jsonify(handle(data.get('description', '')))


if __name__ == '__main__':
    app.run(port=5000)
