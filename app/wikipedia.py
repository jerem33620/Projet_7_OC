# -*- coding: utf-8 -*-
import requests


class WikiP:

    def search_for_pages(self, latitude, longitude):
        """Permet de chercher la page wikipedia, grâce à la latitude et la longitude"""
        params = {
            "action": "query",
            "list": "geosearch",
            "gsradius": 10000,
            "gscoord": f"{latitude}|{longitude}",
            "format": "json",
        }

        url = "https://fr.wikipedia.org/w/api.php"

        r = requests.get(url, params=params)

        if r.status_code == 200:
            data = r.json()
            return data["query"]["geosearch"]
        return []

    def search_for_page_content(self, id):
        """Permet de trouvé le texte correspondant grâce à l'id de la page (pageids)"""
        params = {
            "action": "query",
            "prop": "extracts|info",
            "explaintext": "",
            "pageids": id,
            "inprop": "url",
            "format": "json",
            "exchars": 300,
        }

        url = "https://fr.wikipedia.org/w/api.php"

        r = requests.get(url, params=params)

        if r.status_code == 200:
            data = r.json()
            url_page = data['query']['pages'][str(id)]['fullurl']
            intro = data['query']['pages'][str(id)]['extract']
            return intro, url_page
        return []