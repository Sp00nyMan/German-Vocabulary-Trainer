from DataLoader import get_verbs
from Entities import Verb
from TestBuilder.Tests.Test import Test


class VerbsTranslate(Test):
    _LAYOUT_FILE = "verbs_translate.kv"
    _last_word: Verb

    def __init__(self, footer):
        dictionary = get_verbs()
        super().__init__(footer, dictionary)

        self._infinitive = self.ids['inf']

    def _clear(self):
        super()._clear()
        self._infinitive.text = ""
        self._infinitive.error = False
        self._infinitive.hint_text = "Infinitiv"

        self.ids['translation'].text = self._last_word.translation

    def _focus(self):
        self._infinitive.focus = True

    def check(self, user_guess):
        if not VerbsTranslate._compare(self._last_word, user_guess):
            return ['inf']
        return []

    @staticmethod
    def _compare(word1: Verb, word2):
        assert isinstance(word1, Verb)
        if isinstance(word2, tuple):
            word2 = Verb(word2[0], None)
        if isinstance(word2, Verb):
            return word1.infinitive == word2.infinitive
        raise ValueError(f"word2 has unsupported type: {type(word2)}")

    def _from_series(self, word_series):
        return Verb(*word_series.tolist())

    def _get_word_for_hint(self) -> str:
        return self._last_word.infinitive

    def get_user_input(self):
        return self._infinitive.text,

    def _set_hint(self, hint: str):
        self._infinitive.hint_text = hint
