from Entities import Word

trennbare_prefixe = ("an", "auf", "ab", "aus", "bei", "da", "ein",
                     "mit", "vor", "zu", "hin", "her", "nach", "los",
                     "weiter", "rein", "raus", "weg", "gegen", "hoch",
                     "runter", "rüber", "entlang", "empor", "entgegen",
                     "fern", "fest", "fort", "nieder", "zurecht", "zusammen",
                     "auseinander", "entzwei", "gegenüber", "heim", "hinterher")

untrennbare_prefixe = ("ge", "be", "zer", "ver", "ent", "er", "re",
                       "de", "des", "dis", "in", "miss", "fehl", "hinter")


class Verb(Word):
    def __init__(self, infinitive: str, translation: str, synonyms: str):
        super().__init__(translation, synonyms)
        self._infinitive = infinitive.strip().lower()

    def __str__(self):
        return f"{self.infinitive} - {self._translation}"

    @property
    def infinitive(self):
        return self._infinitive
