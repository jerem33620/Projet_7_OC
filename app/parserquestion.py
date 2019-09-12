# -*- coding: utf-8 -*-
import json

class QuestionParser:
    """C'est la class qui va filtré la question pausé par l'utilisateur"""

    def __init__(self, sentence):
        self.sentence = sentence

    def clean(self):
        """Permet de clean toutes les fonctions"""
        self.transform_to_lowercase()
        self.remove_special()
        self.remove_accents()
        self.delete_spaces()
        return self.sentence

    def transform_to_lowercase(self):
        """Permet de modifié les majuscules en minuscule"""
        str = "CECI EST UN EXEMPLE EN MAJUSCULE"
        return str.lower()

    def remove_special(self):
        """Change tous ces caractères spéciaux en un espace vide"""
        intab = ",?;.:/!-*+%$€_£¤=@|°}]¨[(){'#~&²"
        outab = "                                "
        trantab = str.maketrans(intab, outab)
        return (",?;.:/!-*+%$€_£¤=@|°}]¨[(){'#~&²".translate(trantab))

    def remove_accents(self):
        """Permet de changé les lettres avec accents et de les modifié sans accents"""
        intab = "éèêëãàäâåîïìöôòõñûüÿ"
        outab = "eeeeaaaaaiiioooonuuy"
        trantab = str.maketrans(intab, outab)
        return ("éèêëãàäâåîïìöôòõñûüÿ".translate(trantab))

    def delete_spaces(self):
        """Permet de remplacé plusieurs espaces vides par un seul espace vide et aussi l'apostrophe"""
        delete_spaces = "   j'ai un   probleme avec   mon exemple    "
        return delete_spaces.strip().replace("  ", " ").replace("'", " ")

    def remove_stop_words(self):
        """
        Permet d'ouvrir le fichier json et de filtré les mots dans une liste
        """
        with open('stop_words.json', 'r') as f:
            stop_words = json.load(f)

        cleaned_words = []

        for word in self.sentence.split():
            if word not in stop_words:
                cleaned_words.append(word)
        self.sentence = " ".join(cleaned_words)
