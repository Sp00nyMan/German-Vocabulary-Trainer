from typing import Tuple

from Entities import Word, IrregularVerb
from .Test import Test
from DataLoader import get_irregular_verbs


class VerbsKonjugate(Test):
    _LAYOUT_FILE = "verbs_konjugate.kv"

    def __init__(self, footer):
        dictionary = get_irregular_verbs()
        super().__init__(footer, dictionary)

        self.present = self.ids['pres3']
        self.preteritum = self.ids['pret']
        self.hs = self.ids['hs']
        self.partizip2 = self.ids['part2']

    @staticmethod
    def _compare(word1: Word, word2):
        assert isinstance(word1, IrregularVerb)
        if isinstance(word2, tuple):
            word2 = IrregularVerb(word1.infinitive, *word2, None, None)
        if isinstance(word2, IrregularVerb):
            return word1.present == word2.present, \
                   word1.preteritum == word2.preteritum, \
                   word1.haben_sein == word2.haben_sein, \
                   word1.particle2 == word2.particle2
        raise ValueError(f"word2 has unsupported type: {type(word2)}")

    def check(self, user_guess):
        compare_result = VerbsKonjugate._compare(self._last_word, user_guess)
        incorrect_fields = []
        if not compare_result[0]:
            incorrect_fields.append("pres3")
        if not compare_result[1]:
            incorrect_fields.append("pret")
        if not compare_result[2]:
            incorrect_fields.append("hs")
        if not compare_result[3]:
            incorrect_fields.append("part2")
        return incorrect_fields

    def _clear(self):
        super(VerbsKonjugate, self)._clear()

        self.present.text = ""
        self.present.hint_text = "Präsens"
        self.present.error = False

        self.preteritum.text = ""
        self.preteritum.hint_text = "Präteritum"
        self.preteritum.error = False

        self.hs.text = ""
        self.hs.hint_text = "haben/sein"
        self.hs.error = False

        self.partizip2.text = ""
        self.partizip2.hint_text = "Partizip II"
        self.partizip2.error = False

        self.ids['inf'].text = f"{self._last_word.infinitive} - {self._last_word.translation}"

    def _focus(self):
        self.present.focus = True

    def _from_series(self, word_series):
        return IrregularVerb(*word_series.to_list())

    def _get_word_for_hint(self) -> str:
        return "no"

    def get_user_input(self) -> Tuple:
        return self.present.text, \
               self.preteritum.text, \
               self.hs.text, \
               self.partizip2.text

    def _set_hint(self, hint: str):
        pass
