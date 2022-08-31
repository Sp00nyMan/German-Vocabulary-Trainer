from .Test import Test
from Entities import Adjective
from DataLoader import get_adjectives


class AdjectivesTranslate(Test):
    _LAYOUT_FILE = "adjectives_translate.kv"
    _last_word: Adjective

    def __init__(self, footer):
        dictionary = get_adjectives()
        super().__init__(footer, dictionary)

        self._adjektive = self.ids['adjektive']

    def _clear(self):
        super()._clear()
        self._adjektive.text = ""
        self._adjektive.hint_text = "Adjektive"
        self._adjektive.error = False

        self.ids['translation'].text = self._last_word.translation

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

    def _from_series(self, word_series):
        return Adjective(*word_series.to_list())

    def get_user_input(self):
        return self._adjektive.text,
