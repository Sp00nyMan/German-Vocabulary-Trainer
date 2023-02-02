from typing import Tuple

from DataLoader.DataLoader import get_phrases
from Entities import Word, Phrase
from .Test import Test


class Phrases(Test):
    _LAYOUT_FILE = "phrases.kv"
    _last_word: Phrase

    def __init__(self, footer):
        dictionary = get_phrases()
        super().__init__(footer, dictionary)

        self._phrase = self.ids['phrase']
        self._translation = self.ids['translation']

    @staticmethod
    def _compare(word1: Word, word2):
        assert isinstance(word1, Phrase)
        if isinstance(word2, tuple):
            word2 = Phrase(word2[0], None)
        if isinstance(word2, Phrase):
            if len(word1.phrase) != len(word2.phrase):
                return False
            if word1.phrase != word2.phrase:
                wrong_positions = [i for i, (char, guess) in enumerate(zip(word1.phrase, word2.phrase)) if guess != char]
                return wrong_positions
            return True
        raise ValueError(f"word2 has unsupported type: {type(word2)}")

    def check(self, user_guess):
        compare_result = Phrases._compare(self._last_word, user_guess)
        if compare_result is True:
            return []
        return [compare_result]

    def _clear(self):
        super()._clear()
        self._phrase.text = ""
        self._phrase.error = False
        self._phrase.hint_text = "Phrase"

        self._translation.text = self._last_word.translation

    def _focus(self):
        self._phrase.focus = True

    def _from_series(self, word_series):
        return Phrase(*word_series.to_list())

    def _get_word_for_hint(self) -> str:
        return self._last_word.phrase

    def get_user_input(self) -> Tuple:
        return self._phrase.text,

    def hint(self):
        words_for_hint = self._get_word_for_hint().split(' ')
        if self._hint_chars_to_open > len(words_for_hint):
            return
        hint = " ".join(words_for_hint[:self._hint_chars_to_open])

        for hidden_word in words_for_hint[self._hint_chars_to_open:]:
            hint += " " + "_ " * len(hidden_word)

        self._hint_chars_to_open += 1
        self.subtract_points(1)
        if "_" not in hint:
            self.subtract_points(1)

        self._set_hint(hint.rstrip())
        self._focus()

    def _set_hint(self, hint: str):
        self._phrase.hint_text = hint

    def highlight_red(self, wrong_positions):
        self._phrase.error = True
