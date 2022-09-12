from datetime import datetime


class WordRecord:
    TIME_FORMAT = "%d.%m.%Y %H:%M:%S"

    word_repr: str

    points: int
    _last_shown: datetime

    def __init__(self, *args):
        if len(args) == 1:
            args = self._from_dict(args[0])
        if len(args) == 3:
            self.word_repr, self.points, self.last_shown = args
        else:
            raise ValueError("Invalid arguments")

    @property
    def last_shown(self):
        return self._last_shown

    @last_shown.setter
    def last_shown(self, value):
        if isinstance(value, datetime):
            self._last_shown = value
        elif isinstance(value, str):
            self._last_shown = datetime.strptime(value, WordRecord.TIME_FORMAT)

    def on_shown(self):
        self.points += 1
        self.last_shown = datetime.now()

    def __iadd__(self, other):
        if self.points is None:
            self.points = 0
        self.on_shown()
        self.points += other - 1
        return self

    def to_dict(self):
        """
        :return: key(word_repr), value
        """
        return self.word_repr, {"points": self.points,
                                "last": self.last_shown.strftime(WordRecord.TIME_FORMAT)}

    @staticmethod
    def _from_dict(d):
        assert isinstance(d, dict)
        word_repr = list(d.keys())[0]
        d = d[word_repr]
        if d is not None:
            points = d["points"]
            last_shown = d["last"]
        else:
            points = 0
            last_shown = datetime.now()
        return word_repr, points, last_shown

    def __repr__(self):
        return f"{self.word_repr}: {self.points} - {self.last_shown.strftime(WordRecord.TIME_FORMAT)}"
