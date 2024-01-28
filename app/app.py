from database.database_connection import init_app
from handlers.delete_handler import remove_handle
from handlers.get_handler import list_handle, retrieve_handle
from handlers.post_handler import create_handle
from flask import Flask, request


app = Flask(__name__)


@app.route('/conversions/<element_id>', methods=['DELETE'])
def delete_conversion(element_id):
    return remove_handle(element_id)


@app.route('/conversions/<conversion_id>', methods=['GET'])
def retrieve_conversion(conversion_id):
    return retrieve_handle(conversion_id)


@app.route('/conversions', methods=['POST'])
def create_conversion():
    return create_handle(request)


@app.route('/conversions', methods=['GET'])
def get_conversions():
    return list_handle()


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
    init_app(app)
