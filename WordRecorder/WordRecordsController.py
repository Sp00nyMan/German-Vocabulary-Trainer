import json

from .WordRecord import WordRecord

STATS_FILE = "WordRecorder/stats.json"
_stats: dict = None


def load_stats():
    global _stats
    with open(STATS_FILE, encoding='utf-8') as f:
        _stats = json.load(f)


def save_stats():
    with open(STATS_FILE, "w", encoding='utf-8') as f:
        json.dump(_stats, f, indent=4)
    print("STATS SAVED SUCCESSFULLY!!!")


def get_record(word):
    word_repr = str(word)
    record_dict = _stats["shown"].get(word_repr, None)
    return WordRecord({word_repr: record_dict})


def update_record(word, add=1):
    wr = get_record(word)
    wr += add
    _stats["shown"][str(word)] = wr.to_dict()[1]


def compare(word1, word2):
    """
    :return: the word that has been show less times
    """
    record1 = get_record(word1)
    record2 = get_record(word2)
    if record1.count_shown < record2.count_shown or \
            record1.count_shown == record2.count_shown and record1.last_shown < record2.last_shown:
        return word1
    return word2
