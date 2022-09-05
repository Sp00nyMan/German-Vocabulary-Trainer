from datetime import datetime


class WordRecord:
    TIME_FORMAT = "%d.%m.%Y %H:%M:%S"

    word_repr: str

    count_shown: int
    _last_shown: datetime

    def __init__(self, *args):
        if len(args) == 1:
            args = self._from_dict(args[0])
        if len(args) == 3:
            self.word_repr, self.count_shown, self.last_shown = args
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
        self.count_shown += 1
        self.last_shown = datetime.now()

    def __iadd__(self, other):
        if self.count_shown is None:
            self.count_shown = 0
        self.on_shown()
        self.count_shown += other - 1
        return self

    def to_dict(self):
        """
        :return: key(word_repr), value
        """
        return self.word_repr, {"count": self.count_shown,
                                "last": self.last_shown.strftime(WordRecord.TIME_FORMAT)}

    @staticmethod
    def _from_dict(d):
        assert isinstance(d, dict)
        word_repr = list(d.keys())[0]
        d = d[word_repr]
        if d is not None:
            count_shown = d["count"]
            last_shown = d["last"]
        else:
            count_shown = 0
            last_shown = datetime.now()
        return word_repr, count_shown, last_shown

    def __repr__(self):
        return f"{self.word_repr}: {self.count_shown} - {self.last_shown.strftime(WordRecord.TIME_FORMAT)}"
