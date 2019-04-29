""" main.GrandPyBot test """

# -*- coding: utf-8 -*-
from main import GrandPyBot

class TestGrandPyBot():

    def setup(self):
        """ Cette méthode crée une instance de GrandPyBot. """
        self.grandpybot = GrandPyBot()

    def test_grandpybot(self):
        """ Cette méthode teste si l'instance créer est de type (GrandPyBot) """
        assert type(self.grandpybot) == GrandPyBot
