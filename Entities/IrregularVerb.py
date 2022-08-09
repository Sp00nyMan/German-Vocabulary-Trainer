from Entities import Verb


class IrregularVerb(Verb):
    def __init__(self, infinitive: str, translation: str, present: str, imperfekt: str, particle2: str,
                 haben_sein: bool = False):
        super().__init__(infinitive, translation)
        self._present = present.strip() if present else None
        self.imperfekt = imperfekt.strip()
        self.haben_sein = haben_sein
        self.particle2 = particle2.strip()