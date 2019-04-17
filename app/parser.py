import json

# -tc- Prochaine étape: utiliser la méthode clean() pour nettoyer des questions
# -tc- exemples et envoyer le résultat de ce nettoyage à l'api de google
# -tc- maps pour voir si le nettoyage est suffisant.

# -tc- Plutôt QuestionParser. Ne pas utiliser de _ dans les noms de classe
class QuestionParser:

    def __init__(self, sentence):
        self.sentence = sentence

    def clean(self):
        self.transform_to_lowercase()
        # -tc- ces appels n'exécutent pas les méthodes. Il faut des () pour
        # -tc- que l'exécution soit effective.
        self.remove_special()
        self.remove_accents()
        self.delete_spaces(self)

    def transform_to_lowercase(self):
        self.sentence = self.sentence.lower()
        return self.sentence

    def remove_special(self):
        """
        """
        intab = ",?;.:/!-*+%$€_£¤=@|°}]¨[(){'#~&²"
        outab = "                                "
        delete = str.maketrans(intab, outab)
        self.sentence = self.sentence.translate(delete)
        return self.sentence

    def remove_accents(self):
        intab = "éèêëãàäâåîïìöôòõñûüÿ"
        outab = "eeeeaaaaaiiioooonuuy"
        delete = str.maketrans(intab, outab)
        self.sentence = self.sentence.translate(delete)
        return self.sentence

    def delete_spaces(self, sentence):
        remove_spaces = sentence.strip().replace("  ", " ").replace("'", " ")
        return remove_spaces

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

