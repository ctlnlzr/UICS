from flask import jsonify, request
import requests

fuseki_endpoint = "http://localhost:3030/ds/query"


def query_sparql(query):
    try:
        # Get the SPARQL query from the request JSON

        # Send the SPARQL query to the Fuseki endpoint
        response = requests.post(
            fuseki_endpoint,
            headers={'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'},
            data={'query': query}
        )

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            result = response.json()
            return jsonify(result)
        else:
            return jsonify({'error': 'SPARQL query failed'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500
