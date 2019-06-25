# -*- coding: utf-8 -*-
from app import parser

class TestParser:
    """Ici on va testé que le fichier parser, transforme bien les majuscules en minuscule,
    qu'il enlève les espaces en trop, qu'il enlève les caractères spéciales et les remplaces
    par un espace et qu'il change les lettres avec accents en lettres sans accents."""

    def test_transform_to_lowercase(self):
        ab = parser.QuestionParser("TEST")
        assert ab.transform_to_lowercase() == "test"

    def test_delete_spaces(self):
        ab = parser.QuestionParser("   bla bla   ")
        assert ab.delete_spaces() == "bla bla"
 
    def test_remove_special(self):
        ab = parser.QuestionParser(",?;.:/!-*+%$€_£¤=@|°}]¨[(){'#~&²")
        assert ab.remove_special() == "                                "

    def test_remove_accents(self):
        ab = parser.QuestionParser("éèêëãàäâåîïìöôòõñûüÿ")
        assert ab.remove_accents() == "eeeeaaaaaiiioooonuuy"
