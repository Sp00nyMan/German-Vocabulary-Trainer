from Entities import Word


class Adjective(Word):
    def __init__(self, adjective: str, translation: str, synonyms: str, comparative: str = None, superlative: str = None):
        super().__init__(translation, synonyms)
        self._adjective = adjective.strip().lower() if adjective else None
        self._comparative = comparative.strip().lower() if comparative else None
        self._superlative = superlative.strip().lower() if superlative else None

    @property
    def adjective(self):
        return self._adjective

    @property
    def comparative(self):
        return self._comparative

    @property
    def superlative(self):
        return self._superlative

    def __str__(self):
        return f"{self.adjective} - {self.translation}"
