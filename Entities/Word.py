from abc import ABC, abstractmethod


class Word(ABC):
    def __init__(self, translation: str):
        self._translation = translation.strip().lower() if translation else None

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def translation(self):
        return self._translation

