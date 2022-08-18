from typing import Tuple

from kivymd.uix.screen import MDScreen

import DataLoader
from Entities import Word, Verb
from TestBuilder.Tests.Test import Test


class RegularVerbsTranslate(Test):
    LAYOUT_FILE = "regular_verbs_translate.kv"
    _last_word: Verb

    def __init__(self, test_screen: MDScreen):
        dictionary = DataLoader.get_regular_verbs()
        super().__init__(test_screen, dictionary)

    def _clear(self):
        super()._clear()
        self._test_screen.ids['inf'].text = ""
        self._test_screen.ids['inf'].error = False
        self._test_screen.ids['inf'].hint_text = "Infinitive"

        self._test_screen.ids['translation'].text = self._last_word.translation

    def _focus(self):
        self._test_screen.ids['inf'].focus = True

    def check(self, user_guess):
        if not RegularVerbsTranslate._compare(self._last_word, user_guess):
            return ['inf']
        return []

    @staticmethod
    def _compare(word1: Word, word2):
        assert isinstance(word1, Verb)
        if isinstance(word2, tuple):
            word2 = Verb(word2[0], None)
        if isinstance(word2, Verb):
            return word1.infinitive == word2.infinitive
        raise ValueError(f"word2 has unsupported type: {type(word2)}")

    def __next__(self):
        _, verb = next(self.dictionary)
        verb = Verb(*verb.tolist())

        self._last_word = verb
        self._clear()

        return verb

    def _get_word_for_hint(self) -> str:
        return self._last_word.infinitive

    def get_user_input(self) -> Tuple:
        return self._test_screen.ids['inf'].text,

    def _set_hint(self, hint: str):
        self._test_screen.ids['inf'].hint_text = hint

