from Entities import Word

class Adverb(Word):
    def __init__(self, adjective: str, translation: str):
        super().__init__(translation)
        self.adverb = adjective.strip()