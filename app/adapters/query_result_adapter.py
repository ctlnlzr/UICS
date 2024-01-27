from flask import jsonify, make_response


def convert_output(query_result):
    if query_result.status_code == 200:
        return create_response(get_output(query_result), 200)
    else:
        return create_response("Failed SPARQL request", 500)


def create_response(message, status_code):
    response_data = {'message': message}

    return make_response(jsonify(response_data), status_code)


def get_output(query_result):
    return query_result.json['results']['bindings'][0]['code']['value'].replace("\n", "")


