from Entities import Word


class Adverb(Word):
    def __init__(self, adjective: str, translation: str, synonyms: str):
        super().__init__(translation, synonyms)
        self._adverb = adjective.strip().lower()

    @property
    def adverb(self):
        return self._adverb

    def __str__(self):
        return f"{self.adverb} - {self.translation}"
