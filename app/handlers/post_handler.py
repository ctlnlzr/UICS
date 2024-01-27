from adapters.controlled_language_adapter import convert_input
from adapters.query_result_adapter import convert_output
from adapters.sparql_adapter import query_sparql


def handle(request):
    description = request.get_json().get('description', '')
    return convert_output(query_sparql(convert_input(description)))
