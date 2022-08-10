import pandas as pd
from kivymd.uix.screen import MDScreen

import DataLoader as dl
from Entities import Noun, Word


class TestBuilder:

    def __init__(self, test_screen: MDScreen, mode: str):
        self._test_screen = test_screen
        self._dictionary: pd.DataFrame = None

        match mode.lower():
            case "nouns_translate":
                self.update_screen, self.__next__ = self._nouns_translate()
            case _:
                raise ValueError("Unsupported mode")

    @staticmethod
    def _nouns_translate():
        def comparison(one: Noun, other: Noun):
            return one.singular == other.singular and one.translation == other.translation

        def update_screen(test_screen: MDScreen, new_word: Word):
            test_screen.ids['translation'].text = new_word.translation
        dictionary = dl.get_nouns()
        dictionary.reset_index()
        dictionary = dictionary.sample(frac=1).iterrows()

        def next_item():
            _, noun = next(dictionary)
            noun = noun.tolist()
            noun = Noun(*noun, comparison_function=comparison)
            return noun

        return update_screen, next_item