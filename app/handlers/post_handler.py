from adapters.controlled_language_adapter import convert_input
from adapters.result_adapter import create_response
from adapters.sparql_adapter import query_sparql
from database.access import insert_conversion
import uuid


def create_handle(request):
    description = request.get_json().get('description', '')
    return get_output(query_sparql(convert_input(description)))


def persist_answer(query_result):
    conversion_id = str(uuid.uuid4())
    if insert_conversion(conversion_id, query_result) is None:
        return {'id': conversion_id, 'message': query_result}, 201
    else:
        return {'message': "Database insertion failed"}, 500


def extract_code(query_result):
    if len(query_result.json['results']['bindings']) > 0:
        return query_result.json['results']['bindings'][0]['code']['value'].replace("\n", "")
    return None


def get_output(query_result):
    if query_result.status_code == 200:
        answer = extract_code(query_result)
        if answer is not None:
            answer = persist_answer(answer)
            return create_response(answer[0], answer[1])
        else:
            return create_response({"message": "No results"}, 200)
    else:
        return create_response({"message": "Failed SPARQL request"}, 500)


