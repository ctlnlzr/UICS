from flask import Flask, request
from handlers.post_handler import handle
from flask import Flask, jsonify, request
import sqlite3
import os

app = Flask(__name__)


@app.route('/conversion', methods=['POST'])
def post():
    return handle(request)

def connect_db():
    return sqlite3.connect(DATABASE)


@app.route('/')
def test():
    return 'Test yay'


@app.route('/elements', methods=['GET'])
def list_elements():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM elements')
        elements = cursor.fetchall()
        element_list = [{'id': row[0], 'generatedCode': row[1]} for row in elements]

        conn.close()
        return jsonify({'Elements': element_list})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/elements', methods=['POST'])
def add_element():
    try:
        data = request.json
        if 'id' not in data or 'generatedCode' not in data:
            return jsonify({'error': 'Invalid input data'}), 400

        element_id = data['id']
        generated_code = data['generatedCode']

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute('INSERT INTO elements (id, generatedCode) VALUES (?, ?)', (element_id, generated_code))
        conn.commit()

        cursor.execute('SELECT * FROM elements WHERE id = ?', (element_id,))
        inserted_element = cursor.fetchone()
        conn.close()
        return jsonify({'id': inserted_element[0], 'generatedCode': inserted_element[1]}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/elements/<element_id>', methods=['GET'])
def get_element(element_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM elements WHERE id = ?', (element_id,))
        element = cursor.fetchone()
        conn.close()

        if element:
            return jsonify({'id': element[0], 'generatedCode': element[1]})
        else:
            return jsonify({'error': 'Element not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/elements/<element_id>', methods=['DELETE'])
def delete_element(element_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute('DELETE FROM elements WHERE id = ?', (element_id,))
        conn.commit()
        conn.close()

        return jsonify({'Element deleted'}), 204
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
    DATABASE = os.path.join(PROJECT_ROOT, 'database', 'conversions.db')
    app.run(port=5000, debug=True)
