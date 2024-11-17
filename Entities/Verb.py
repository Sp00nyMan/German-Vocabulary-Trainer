from enum import Enum
from Entities import Word

trennbare_prefixe = ("an", "auf", "ab", "aus", "bei", "da", "ein",
                     "mit", "vor", "zu", "hin", "her", "nach", "los",
                     "weiter", "rein", "raus", "weg", "gegen", "hoch",
                     "runter", "rüber", "entlang", "empor", "entgegen",
                     "fern", "fest", "fort", "nieder", "zurecht", "zusammen",
                     "auseinander", "entzwei", "gegenüber", "heim", "hinterher")

untrennbare_prefixe = ("ge", "be", "zer", "ver", "ent", "er", "re",
                       "de", "des", "dis", "in", "miss", "fehl", "hinter")


prepositions = ("auf + Dat.", "auf + Akk.", "an + Dat.", "an + Akk.", "in + Dat.", "in + Akk.", "über", "von", "mit", "nach", "um", "aus", "zu", "vor", "bei", "für", "durch")    

class IrregularityGroup(Enum):
    REGULAR = "regular"
    EAO = "e-a-o"
    EAA = "e-a-a"
    EII = "e-i-i"
    EIA = "e-i-a"
    EIO = "e-i-o"
    IAU = "i-a-u"
    IAO = "i-a-o"
    IAE = "i-a-e"
    IOO = "i-o-o"
    IAA = "i-a-a"
    EIIEIE = "ei-ie-ie"
    IEAO = "ie-a-o"
    IEOO = "ie-o-o"
    IEAE = "ie-a-e"
    AIEA = "a-ie-a"
    AEUA = "ä-u-a"
    AEIA = "ä-i-a"
    UEOO = "ü-o-o"
    OEOO = "ö-o-o"

    

class Verb(Word):
    def __init__(self, infinitive: str, translation: str, preposition: str = None, irregularity: str = None, synonyms: str = None):
        super().__init__(translation, synonyms)
        self.preposition = preposition
        self.irregularity = IrregularityGroup(irregularity if irregularity is not None else "regular")
        self.infinitive = infinitive.strip().lower()

    def __str__(self):
        return f"{self.infinitive} + {self.preposition} - {self._translation}"
