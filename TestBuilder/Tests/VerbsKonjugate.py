from typing import Tuple

from Entities import Word, IrregularVerb
from .Test import Test
from DataLoader import get_irregular_verbs


class VerbsKonjugate(Test):
    _last_word: IrregularVerb
    _LAYOUT_FILE = "verbs_konjugate.kv"

    _hint_opened: dict

    def __init__(self, footer):
        dictionary = get_irregular_verbs()
        super().__init__(footer, dictionary)

        self.present = self.ids['pres3']
        self.preteritum = self.ids['pret']
        self.hs = self.ids['hs']
        self.partizip2 = self.ids['part2']

        self.__last_incorrect = None

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
        self.__last_incorrect = incorrect_fields
        return incorrect_fields

    def _clear(self):
        super(VerbsKonjugate, self)._clear()

        self._hint_opened = dict()

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

    def get_user_input(self) -> Tuple:
        return self.present.text, \
               self.preteritum.text, \
               self.hs.text, \
               self.partizip2.text

    def _get_word_for_hint(self) -> str:
        raise NotImplementedError()

    def _set_hint(self, hint: str):
        raise NotImplementedError()

    def __get_word_for_hint(self, field):
        match field:
            case "pres3":
                return self._last_word.present
            case "pret":
                return self._last_word.preteritum
            case "hs":
                return self._last_word.haben_sein
            case "part2":
                return self._last_word.particle2

    def __set_hint(self, hint, field):
        match field:
            case "pres3":
                field = self.present
            case "pret":
                field = self.preteritum
            case "part2":
                field = self.partizip2
            case _:
                return
        field.hint_text = hint

    def hint(self):
        for field in self.__last_incorrect:
            word_for_hint = self.__get_word_for_hint(field)

            left_to_open = []
            if field not in self._hint_opened:
                self._hint_opened[field] = set()
            for c in set(word_for_hint.lower()):  # Not using set because I want to preserve the order of the letters
                if c not in self._hint_opened[field] and c not in left_to_open:
                    left_to_open.append(c)

            self._hint_opened[field].add(left_to_open.pop(0))

            hint = ""
            for c in word_for_hint:
                hint += (c if c.lower() in self._hint_opened[field] else '_') + ' '

            self.subtract_points(1)
            self.__set_hint(hint.rstrip(), field)
        self._focus()
