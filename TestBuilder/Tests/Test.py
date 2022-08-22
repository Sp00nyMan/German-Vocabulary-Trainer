from abc import ABC, abstractmethod
from typing import Tuple

from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import MDScreen

from Entities import Word


class Test(ABC, BoxLayout):
    LAYOUT_FILE: str

    def __init__(self, test_screen: MDScreen, dictionary):
        super().__init__()
        self._test_screen: MDScreen = test_screen
        self.dictionary = dictionary

        self._last_word: Word = None
        self._hint = self._test_screen.ids['footer'].ids['hint']

    @staticmethod
    @abstractmethod
    def _compare(word1: Word, word2):
        pass

    @abstractmethod
    def check(self, user_guess):
        """
        :param user_guess: user's input in the fields genus and singular
        :return: the list of fields' ids that are incorrect
        """
        pass

    @abstractmethod
    def _clear(self):
        self._focus()

        self._hint_opened = set()
        self._hint_chars_to_open = 1

        self._hint.disabled = True
        self._hint.opacity = 0

    @abstractmethod
    def _focus(self):
        pass

    def enable_hint_button(self):
        self._hint.disabled = False
        self._hint.opacity = 1

    @abstractmethod
    def __next__(self):
        pass

    def __iter__(self):
        return self

    @abstractmethod
    def _get_word_for_hint(self) -> str:
        pass

    @abstractmethod
    def get_user_input(self) -> Tuple:
        pass

    @abstractmethod
    def _set_hint(self, hint: str):
        pass

    def hint(self):
        word_for_hint = self._get_word_for_hint()
        left_to_open = []
        for c in word_for_hint.lower():  # Not using set because I want to preserve the order of the letters
            if c not in self._hint_opened and c not in left_to_open:
                left_to_open.append(c)
        chars_count = len(left_to_open)

        for _ in range(min(int(self._hint_chars_to_open), len(left_to_open))):
            self._hint_opened.add(left_to_open.pop(0))

        hint = ""
        for c in word_for_hint:
            hint += (c if c in self._hint_opened or c.lower() in self._hint_opened else '_') + ' '

        if self._hint_chars_to_open < chars_count:
            self._hint_chars_to_open += 0.5

        self._set_hint(hint.rstrip())
