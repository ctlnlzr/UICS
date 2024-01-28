from adapters.result_adapter import create_response
from database.access import remove_conversion


def remove_handle(conversion_id):
    if remove_conversion(conversion_id) is None:
        return create_response({"message": "Deletion succeeded"}, 204)
    else:
        return create_response({"message": "Database error"}, 500)
