from app.adapters.controlled_language_adapter import convert_input
from app.adapters.query_result_adapter import convert_output
from app.adapters.sparql_adapter import query_sparql


def handle(description):
    result = query_sparql(convert_input(description))
    if result.status_code == 200:
        return convert_output(result.json())
    else:
        return "Failed SPARQL request"
