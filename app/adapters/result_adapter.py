from flask import jsonify, make_response


def create_response(response_data, status_code):
    return make_response(jsonify(response_data), status_code)



