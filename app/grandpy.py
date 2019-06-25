# -*- coding: utf-8 -*-
from app.parser import QuestionParser
from app.googlemaps import GMaps
from app.wikipedia import WikiP


def question_for_app_grandpy(question):
    """C'est le fichier qui permet de répondre à la question pausé sur le site web"""
    parser = QuestionParser(question)
    question = parser.clean()
    gmaps = GMaps()
    result_address = gmaps.search(question)
    wikip = WikiP()
    pages = wikip.search_for_pages(result_address["latitude"], result_address["longitude"])
    result_wiki = wikip.search_for_page_content(pages[0]["pageid"])
    return {
        "parser": question,
        "gmaps": result_address,
        "wikimedia": result_wiki
    }
