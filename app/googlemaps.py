# -*- coding: utf-8 -*-
import os
import googlemaps


class GMaps:
    
    def __init__(self):
        """Permet de générer la clé de l'API de googlemaps"""
        self.gmaps = googlemaps.Client(key=os.getenv("GOOGLEMAPS_API_KEY"))

    def search(self, sentence):
        """Permet d'obtenir l'adress voulut grâce à la latitude et la longitude"""
        results = self.gmaps.geocode(sentence)
        if results: 
            result = results[0]
            final_result = {
                "address": result["formatted_address"],
                "latitude": result["geometry"]["location"]["lat"],
                "longitude": result["geometry"]["location"]["lng"]
            }
            return final_result
        return {"address":None, "latitude":None, "longitude":None}
