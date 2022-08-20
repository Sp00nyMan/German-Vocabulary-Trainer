from typing import Tuple

from kivymd.uix.screen import MDScreen

from Entities import Adjective
from GUI.screens.TestScreen import TextField
from .Test import Test
from DataLoader import get_adjectives


class AdjectivesTranslate(Test):
    LAYOUT_FILE = "adjectives_translate.kv"
    _last_word: Adjective

    def __init__(self, test_screen: MDScreen):
        dictionary = get_adjectives()
        super().__init__(test_screen, dictionary)

        self._adjektive: TextField = self._test_screen.ids['adjektive']

    def _clear(self):
        super()._clear()
        self._adjektive.text = ""
        self._adjektive.hint_text = "Adjektive"
        self._adjektive.error = False

        self._test_screen.ids['translation'].text = self._last_word.translation

    def _focus(self):
        self._adjektive.focus = True

    def check(self, user_guess):
        if not AdjectivesTranslate._compare(self._last_word, user_guess):
            return ['adjektive']
        return []

    @staticmethod
    def _compare(word1: Adjective, word2):
        assert isinstance(word1, Adjective)
        if isinstance(word2, tuple):
            word2 = Adjective(word2[0], *[None]*3)
        if isinstance(word2, Adjective):
            return word1.adjective == word2.adjective
        raise ValueError(f"word2 has unsupported type: {type(word2)}")

    def _get_word_for_hint(self) -> str:
        return self._last_word.adjective

    def _set_hint(self, hint):
        self._focus()
        self._adjektive.hint_text = hint

    def __next__(self):
        _, adjective = next(self.dictionary)
        adjective = adjective.tolist()
        adjective = Adjective(*adjective)

        self._last_word = adjective
        self._clear()

        return adjective

    def get_user_input(self):
        return self._adjektive.text,
