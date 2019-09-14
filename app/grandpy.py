# -*- coding: utf-8 -*-
import random

from .parserquestion import QuestionParser
from .gomaps import GMaps
from .wikipedia import WikiP
from .reponsegrandpy import *


def question_for_app_grandpy(question):
    """C'est le fichier qui permet de répondre à la question pausé sur le site web"""
    parser = QuestionParser(question)
    question = parser.clean()
    gmaps = GMaps()
    result_address = gmaps.search(question)
    wikip = WikiP()
    pages = wikip.search_for_pages(result_address["latitude"], result_address["longitude"])
    result_article, result_url = wikip.search_for_page_content(pages[0]["pageid"])
    return {
        "grandpy": random.choice(reponseListe),
        "parser": question,
        "gmaps": result_address,
        "wikip": result_article,
        "wikip_url": result_url,
    }
