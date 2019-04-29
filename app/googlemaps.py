# -*- coding: utf-8 -*-
import os
import googlemaps
from datetime import datetime
from app.parser import QuestionParser

class GMaps:
    
    def __init__(self):
        
        self.gmaps = googlemaps.Client(key=os.getenv("GOOGLEMAPS_API_KEY"))

    def search(self,sentence):
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

def main():
    sentence = "Tour Eiffel?"
    parser = QuestionParser(sentence)
    gmaps = GMaps()
    print(gmaps.search(parser.clean()))
    

if __name__ == "__main__":
    main()