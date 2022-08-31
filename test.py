import json
from time import sleep

from WordRecorder import WordRecord


def main():
    with open("DataLoader/stats.json") as f:
        wr_j = json.load(f)
    mode = "nouns_translate"
    word = "das Bild"
    wr = WordRecord({mode: {word: wr_j["shown_by_mode"][mode][word]}})
    print(wr.to_dict())
    wr.on_shown()
    print(wr.to_dict())
    sleep(10)
    wr.on_shown()
    print(wr.to_dict())
    w = wr.to_dict()
    wr_j["shown_by_mode"][mode][w[0]] = w[1]
    with open("DataLoader/stats.json", "w") as f:
        json.dump(wr_j, f, indent=4)


if __name__ == '__main__':
    main()
    main()
