from typing import Tuple

from kivymd.uix.screen import MDScreen

from DataLoader import get_nouns
from Entities import Word, Noun
from TestBuilder.Tests.Test import Test


class NounsPlural(Test):
    _LAYOUT_FILE = "nouns_plural.kv"
    _last_word: Noun

    def __init__(self, test_screen: MDScreen):
        dictionary = get_nouns()
        super().__init__(test_screen, dictionary)

        self._plural = self.ids['plural']

    @staticmethod
    def _compare(word1: Word, word2):
        assert isinstance(word1, Noun)
        if isinstance(word2, tuple):
            word2 = Noun(*[None]*2, word2[0], None)
        if isinstance(word2, Noun):
            return word1.plural == word2.plural
        raise ValueError(f"word2 has unsupported type: {type(word2)}")

    def check(self, user_guess):
        if not NounsPlural._compare(self._last_word, user_guess):
            return ['plural']
        return []

    def _clear(self):
        super()._clear()
        self._plural.text = ""
        self._plural.hint_text = "Plural"
        self._plural.error = False

        self.ids['genus_singular'].text = f"{self._last_word.gender} {self._last_word.singular}"
        self.ids['translation'].text = self._last_word.translation

    def _focus(self):
        self._plural.focus = True

    def __next__(self):
        _, noun = next(self.dictionary)
        if not noun.plural:
            noun.plural = noun.singular
        noun = noun.tolist()
        noun = Noun(*noun)

        self._last_word = noun
        self._clear()

        return noun

    def _get_word_for_hint(self) -> str:
        return self._last_word.plural

    def get_user_input(self) -> Tuple:
        return self._plural.text,

    def _set_hint(self, hint: str):
        self._plural.hint_text = hint