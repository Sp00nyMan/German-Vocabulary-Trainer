from enum import Enum
from Entities import Word


class Gender(Enum):
    FEMININE = "die"
    MASCULINE = "der"
    NEUTRAL = "das"

    def __str__(self):
        return self.value


class Noun(Word):

    def __init__(self, gender: Gender, singular: str, plural: str, translation: str, comparison_function=None):
        super().__init__(translation, comparison_function)
        self._gender = Gender(gender)
        self._singular = singular.strip().lower()
        self._plural = plural.strip().lower() if plural else None

    @property
    def gender(self):
        return self._gender

    @property
    def translation(self):
        return self._translation

    @property
    def singular(self):
        return f"{self.gender} {self._singular.capitalize()}" if self._singular else None

    @property
    def plural(self):
        return self._plural.capitalize() if self._plural else None

    def __str__(self):
        return f"{self.singular}, {self.plural} - {self.translation}"
