import json
from app import gomaps


def test_search_for_latitude_longitude(monkeypatch):
    """Ici on va testé que le fichier gomaps cherche bien la latitude, la longitude et l'address"""
    address = 'Champ de mars, 5 Avenue Anatole France, 75007 Paris, France'
    latitude = 48.85837009999999
    longitude = 2.2944813
    results = [{
            "formatted_address": address,
            "geometry": {"location":{"lng": longitude, "lat": latitude}}
            }
        ]

    class MockClient:
        def __init__(self, key):
            pass

        def geocode(self, sentence):
            return results

    monkeypatch.setattr("googlemaps.Client", MockClient)
    gmaps = gomaps.GMaps()
    results = gmaps.search("Salut")

    assert results["address"] == address
    assert results["latitude"] - latitude < 0.0001 
    assert results["longitude"] - longitude < 0.0001