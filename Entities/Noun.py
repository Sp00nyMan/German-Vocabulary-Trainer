from enum import Enum
from Entities import Word


class Gender(Enum):
    FEMININE = "die"
    MASCULINE = "der"
    NEUTRAL = "das"

    def __str__(self):
        return self.value

class Noun(Word):
    def __init__(self, gender: Gender, singular: str, plural: str, translation: str):
        super().__init__(translation)
        self.gender = Gender(gender)
        self._singular = singular.strip().lower()
        self._plural = plural.strip().lower() if plural else None

    def translation(self):
        return self._translation

    def singular(self):
        return f"{self.gender} {self._singular.capitalize()}" if self._singular else None

    def plural(self):
        return self._plural.capitalize() if self._plural else None

    def __str__(self):
        return f"{self.singular()}, {self.plural()} - {self.translation()}"