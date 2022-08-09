from Entities import Word


class Adjective(Word):
    def __init__(self, adjective: str, translation: str, comparative: str, superlative: str):
        super().__init__(translation)
        self.adjective = adjective.strip()
        self.comparative = comparative.strip()
        self.superlative = superlative.strip()