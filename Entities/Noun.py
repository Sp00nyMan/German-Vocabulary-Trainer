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
        self._gender = Gender(gender) if gender else None
        self._singular = singular.strip().lower() if singular else None
        self._plural = plural.strip().lower() if plural else None

    @property
    def gender(self):
        return self._gender

    @property
    def translation(self):
        return self._translation

    @property
    def singular(self):
        return f"{self._singular.capitalize()}" if self._singular else None

    @property
    def plural(self):
        return self._plural.capitalize() if self._plural else None

    def __str__(self):
        return f"{self.gender} {self.singular}, {self.plural} - {self.translation}"
