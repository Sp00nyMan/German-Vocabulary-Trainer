from datetime import datetime
from typing import overload


class WordRecord:
    TIME_FORMAT = "%d.%m.%Y %H:%M:%S"

    test_mode: str
    word_repr: str

    count_shown: int
    last_shown: str

    def __init__(self, *args):
        if len(args) == 1:
            args = self._from_dict(args[0])
        if len(args) == 4:
            self.test_mode, self.word_repr, self.count_shown, self.last_shown = args
        else:
            raise ValueError("Invalid arguments")

    def on_shown(self):
        self.count_shown += 1
        self.last_shown = datetime.now().strftime(WordRecord.TIME_FORMAT)

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
        return self.word_repr, {"count_shown": self.count_shown,
                                "last_shown": self.last_shown}

    @staticmethod
    def _from_dict(d):
        assert isinstance(d, dict)
        test_mode = list(d.keys())[0]
        d = d[test_mode]
        word_repr = list(d.keys())[0]
        d = d[word_repr]
        if d is not None:
            count_shown = d["count_shown"]
            last_shown = d["last_shown"]
        else:
            count_shown = 0
            last_shown = datetime.now().strftime(WordRecord.TIME_FORMAT)
        return test_mode, word_repr, count_shown, last_shown
