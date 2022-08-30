
from kivymd.uix.screen import MDScreen

from Entities import Adverb
from GUI.screens.TestScreen import TextField
from .Test import Test
from DataLoader import get_adverbs


class AdverbsTranslate(Test):
    _LAYOUT_FILE = "adverbs_translate.kv"
    _last_word: Adverb

    def __init__(self, footer):
        dictionary = get_adverbs()
        super().__init__(footer, dictionary)

        self._adverb: TextField = self.ids['adverb']

    def _clear(self):
        super()._clear()
        self._adverb.text = ""
        self._adverb.hint_text = "Adverb"
        self._adverb.error = False

        self.ids['translation'].text = self._last_word.translation

    def _focus(self):
        self._adverb.focus = True

    def check(self, user_guess):
        if not AdverbsTranslate._compare(self._last_word, user_guess):
            return ['adverb']
        return []

    @staticmethod
    def _compare(word1: Adverb, word2):
        assert isinstance(word1, Adverb)
        if isinstance(word2, tuple):
            word2 = Adverb(word2[0], None)
        if isinstance(word2, Adverb):
            return word1.adverb == word2.adverb
        raise ValueError(f"word2 has unsupported type: {type(word2)}")

    def _get_word_for_hint(self) -> str:
        return self._last_word.adverb

    def _set_hint(self, hint):
        self._focus()
        self._adverb.hint_text = hint

    def __next__(self):
        _, adverb = next(self.dictionary)
        adverb = adverb.tolist()
        adverb = Adverb(*adverb)

        self._last_word = adverb
        self._clear()

        return adverb

    def get_user_input(self):
        return self._adverb.text,
