from flask import jsonify
import requests

fuseki_endpoint = "https://triplestore.onrender.com/ds/query"


def query_sparql(query):
    try:
        response = requests.post(
            fuseki_endpoint,
            headers={'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'},
            data={'query': query}
        )

        if response.status_code == 200:
            result = response.json()
            return jsonify(result)
        else:
            return jsonify({'error': 'SPARQL query failed', "status_code": 500})

    except Exception as e:
        return jsonify({'error': str(e), "status_code": 500})
