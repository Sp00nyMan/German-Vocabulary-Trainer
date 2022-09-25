from .Word import Word


class Phrase(Word):

    def __init__(self, phrase: str, translation: str, synonyms: str = None):
        self._phrase = phrase.strip()
        super().__init__(translation, synonyms)

    def __str__(self):
        return f"{self.phrase} - {self.translation}"

    @property
    def phrase(self):
        return self._phrase
