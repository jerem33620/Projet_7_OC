import googlemaps
from datetime import datetime
class GMaps:
    
    gmaps = googlemaps.Client(key='AIzaSyCxfjCH-lW7bpTOFb857wKZKGJyRwRe7-U')

# Géocodage d'une adresse
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Recherchez une adresse avec géocodage inverse
    reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Demander des directions via le transport en commun 
    now = datetime.now()
    directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)