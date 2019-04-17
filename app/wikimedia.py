import requests
from pprint import pprint

class WikiM:
    url = "https://fr.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "prop": "info|extracts",
        "inprop": "url",
        "explaintext": "",
        "exchars": 1200,
        "titles": "Eiffel",
        "format": "json",
    }

    response = requests.get(url, params=params)
    pprint(response.json())