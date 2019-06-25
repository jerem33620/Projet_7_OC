import json
from app import wikipedia


def test_search_for_pages_wikipedia(monkeypatch):
    """Ici on va testé le fichier wikipedia"""
    result = [{'pageid': 6422233, 'ns': 0, 'title': 'Academy of Art University',
     'lat': 37.78785, 'lon': -122.40065, 'dist': 129.9, 'primary': ''},
     {'pageid': 5105544, 'ns':0, 'title': '101 Second Street', 'lat': 37.788139,
     'lon': -122.399056, 'dist': 140.9, 'primary': ''}, {'pageid': 429553, 'ns': 0,
     'title': "Musée d'Art moderne de San Francisco", 'lat': 37.7858, 'lon': -122.4008,
     'dist': 163.4, 'primary': ''}, {'pageid': 2350884, 'ns': 0, 'title': 'Golden Gate University',
     'lat': 37.789062, 'lon': -122.398831, 'dist': 244.1, 'primary': ''}, {'pageid': 4644434,
     'ns': 0, 'title': 'Yerba Buena Center for the Arts', 'lat': 37.7854, 'lon': -122.402,
     'dist': 268.7, 'primary': ''}, {'pageid': 3405328, 'ns': 0,
     'title': 'Liste des plus hautes constructions de San Francisco', 'lat': 37.79,
     'lon': -122.4, 'dist': 338, 'primary': ''}, {'pageid': 3935225, 'ns': 0,
     'title': 'Moscone Center', 'lat': 37.7842, 'lon': -122.402, 'dist': 369.6, 'primary': ''},
     {'pageid': 11091020, 'ns': 0, 'title': 'Oceanwide Center', 'lat': 37.7903, 'lon': -122.3985,
     'dist': 384.3, 'primary': ''}, {'pageid': 9025323, 'ns': 0, 'title': '88 Kearny Street',
     'lat': 37.788688, 'lon': -122.403477, 'dist': 384.7, 'primary': ''}, {'pageid': 9902380,
     'ns': 0, 'title': 'Contemporary Jewish Museum', 'lat': 37.7858, 'lon': -122.404,
     'dist': 401.6, 'primary': ''}]
    json_response = {'batchcomplete': '', 'query': {'geosearch':result }}

    class Mockget:
        def __init__(self, url, params):
            self.status_code = 200

        def json(self):
            return json_response

    monkeypatch.setattr('requests.get', Mockget)
    wikip = wikipedia.WikiP()
    results = wikip.search_for_pages(1, 2)

    assert results == result

def test_search_for_pages_get_404(monkeypatch):

    class Mockget:
        def __init__(self, url, params):
            self.status_code = 404

    monkeypatch.setattr('requests.get', Mockget)
    wikip = wikipedia.WikiP()
    results = wikip.search_for_pages(1, 2)

    assert results == []