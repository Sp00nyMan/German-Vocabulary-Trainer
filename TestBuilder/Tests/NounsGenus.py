from typing import Tuple

from kivymd.uix.screen import MDScreen

from DataLoader import get_nouns
from Entities import Word, Noun
from TestBuilder.Tests.Test import Test


class NounsGenus(Test):
    LAYOUT_FILE = "nouns_genus.kv"
    _last_word: Noun

    def __init__(self, test_screen: MDScreen):
        dictionary = get_nouns()
        super().__init__(test_screen, dictionary)

        self._genus = self._test_screen.ids['genus']

    @staticmethod
    def _compare(word1: Word, word2):
        assert isinstance(word1, Noun)
        if isinstance(word2, tuple):
            word2 = Noun(word2[0], *[None]*3)
        if isinstance(word2, Noun):
            return word1.gender == word2.gender
        raise ValueError(f"word2 has unsupported type: {type(word2)}")

    def check(self, user_guess):
        if not NounsGenus._compare(self._last_word, user_guess):
            return ['genus']
        return []

    def _clear(self):
        super()._clear()
        self._genus.text = ""
        self._genus.hint_text = "Genus"
        self._genus.error = False

        self._test_screen.ids['singular'].text = self._last_word.singular
        self._test_screen.ids['translation'].text = self._last_word.translation

    def _focus(self):
        self._genus.focus = True

    def __next__(self):
        _, noun = next(self.dictionary)
        if not noun.genus or not noun.singular:
            noun = next(self)
        else:
            noun = noun.tolist()
            noun = Noun(*noun)

        self._last_word = noun
        self._clear()

        return noun

    def _get_word_for_hint(self) -> str:
        return self._last_word.gender.value

    def get_user_input(self) -> Tuple:
        return self._genus.text,

    def _set_hint(self, hint: str):
        self._genus.hint_text = "rly?"