from abc import ABC, abstractmethod


class Word(ABC):
    def __init__(self, translation: str, synonyms: str):
        self._translation = translation.strip().lower() if translation else None
        if synonyms:
            self._synonyms = synonyms.split(", ")

    @abstractmethod
    def __str__(self):
        pass

    @property
    def translation(self):
        return self._translation

    @property
    def synonyms(self):
        return self._synonyms