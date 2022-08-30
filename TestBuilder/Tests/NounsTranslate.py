from typing import Tuple

from kivymd.uix.screen import MDScreen

from Entities import Noun
from GUI.screens.TestScreen import TextField
from .Test import Test
from DataLoader import get_nouns


class NounsTranslate(Test):
    _LAYOUT_FILE = "nouns_translate.kv"
    _last_word: Noun

    def __init__(self, footer, **kwargs):
        dictionary = get_nouns()
        super().__init__(footer, dictionary, **kwargs)
        self._genus: TextField = self.ids['genus']
        self._singular: TextField = self.ids['singular']

    def _clear(self):
        super()._clear()
        self._genus.text = ""
        self._genus.error = False

        self._singular.text = ""
        self._singular.hint_text = "Singular"
        self._singular.error = False

        self.ids['translation'].text = self._last_word.translation

    def _focus(self):
        self._genus.focus = True

    def check(self, guess):
        compare_result = NounsTranslate._compare(self._last_word, guess)
        incorrect_fields = []
        if not compare_result[0]:
            incorrect_fields.append('genus')
        if not compare_result[1]:
            incorrect_fields.append('singular')
        return incorrect_fields

    def _get_word_for_hint(self) -> str:
        return self._last_word.singular

    def _set_hint(self, hint):
        self._singular.hint_text = hint

    @staticmethod
    def _compare(word1: Noun, word2) -> Tuple[bool, bool]:
        assert isinstance(word1, Noun)
        if isinstance(word2, tuple):
            try:
                word2 = Noun(word2[0], word2[1], *[None]*2)
            except ValueError:
                return False, True
        if isinstance(word2, Noun):
            return word1.gender == word2.gender, word1.singular == word2.singular
        raise ValueError(f"word2 has unsupported type: {type(word2)}")

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

    def get_user_input(self):
        return self._genus.text, self._singular.text
