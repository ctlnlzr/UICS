from flask import Flask, request
from handlers.post_handler import handle

app = Flask(__name__)


@app.route('/conversion', methods=['POST'])
def post():
    return handle(request)


if __name__ == '__main__':
    app.run(port=5000)
