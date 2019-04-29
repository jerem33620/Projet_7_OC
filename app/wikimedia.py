# -*- coding: utf-8 -*-
import requests
from pprint import pprint
from mediawiki import MediaWiki
from app.parser import QuestionParser


class WikiM:
    def __init__(self):
        self.wikipedia = MediaWiki(lang="fr")