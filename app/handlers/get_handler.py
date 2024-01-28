from adapters.result_adapter import create_response
from database.access import list_conversions, retrieve_conversion


def retrieve_handle(conversion_id):
    conversion = retrieve_conversion(conversion_id)

    if not conversion:
        return create_response({'message': 'Element not found'}, 404)

    if 'error' in conversion:
        return create_response({'message': "Database error"}, 500)
    else:
        return create_response({'id': conversion[0], 'conversion': conversion[1]}, 200)


def list_handle():
    conversions = list_conversions()

    if isinstance(conversions, list):
        return create_response({'conversions': conversions}, 200)

    return create_response({'message': "Database error"}, 500)

