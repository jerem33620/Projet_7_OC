# -*- coding: utf-8 -*-
from app import parserquestion

class TestParser:
    """Ici on va testé que le fichier parser, transforme bien les majuscules en minuscule,
    qu'il enlève les espaces en trop, qu'il enlève les caractères spéciales et les remplaces
    par un espace et qu'il change les lettres avec accents en lettres sans accents."""

    def test_transform_to_lowercase(self):
        ab = parserquestion.QuestionParser("CECI EST UN EXEMPLE EN MAJUSCULE")
        assert ab.transform_to_lowercase() == "ceci est un exemple en majuscule"

    def test_delete_spaces(self):
        ab = parserquestion.QuestionParser("  j'ai un  probleme avec  mon exemple  ")
        assert ab.delete_spaces() == "j'ai un probleme avec mon exemple"
 
    def test_remove_special(self):
        ab = parserquestion.QuestionParser(",?;.:/!-*+%$€_£¤=@|°}]¨[(){'#~&²")
        assert ab.remove_special() == "                                "

    def test_remove_accents(self):
        ab = parserquestion.QuestionParser("éèêëãàäâåîïìöôòõñûüÿ")
        assert ab.remove_accents() == "eeeeaaaaaiiioooonuuy"
