from Entities import Verb


class IrregularVerb(Verb):
    def __init__(self, infinitive: str, present: str, imperfekt: str, haben_sein: str, particle2: str, translation: str, synonyms):
        super().__init__(infinitive, translation, synonyms)
        self._present = present.strip() if present else None
        self._imperfekt = imperfekt.strip()
        self._haben_sein = haben_sein
        self._particle2 = particle2.strip()

    @property
    def present(self):
        return self._present

    @property
    def preteritum(self):
        return self._imperfekt

    @property
    def haben_sein(self):
        return self._haben_sein

    @property
    def particle2(self):
        return self._particle2
