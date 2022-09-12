import os
from abc import abstractmethod
from typing import Tuple

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField

import WordRecorder
from Entities import Word

LAYOUTS_PATH = r"GUI\layouts\tests"


class Test(BoxLayout):
    _LAYOUT_FILE: str
    EXPERIMENTAL_PRIORITIZE = True  # From two random words select ones that were shown less times

    def __init__(self, footer, dictionary, **kwargs):
        Builder.load_file(self.LAYOUT_FILE)
        super(Test, self).__init__(**kwargs)
        self.dictionary = dictionary

        self._last_word: Word = None
        self._hint_button = footer.ids['hint']
        self._submit_button = footer.ids['submit']

        self._earned_points = 1

    @property
    def earned_points(self):
        return self._earned_points

    def subtract_points(self, points):
        self._earned_points -= points

    def unload(self):
        Builder.unload_file(self.LAYOUT_FILE)
        print(f"Unloaded file: {self.LAYOUT_FILE}")

    @property
    def LAYOUT_FILE(self):
        root_dir = os.getcwd()
        return os.path.join(root_dir, LAYOUTS_PATH, self._LAYOUT_FILE)

    @staticmethod
    @abstractmethod
    def _compare(word1: Word, word2):
        pass

    @abstractmethod
    def check(self, user_guess):
        """
        :param user_guess: user's input in the fields genus and singular
        :return: the list of fields' ids that are incorrect, the earned points
        """
        pass

    def _clear(self):
        self._focus()

        self._hint_opened = set()
        self._hint_chars_to_open = 1

        self._hint_button.disabled = True
        self._hint_button.opacity = 0

        self._earned_points = 1

    @abstractmethod
    def _focus(self):
        pass

    def enable_hint_button(self):
        self._hint_button.disabled = False
        self._hint_button.opacity = 1

    def submit(self):
        self._submit_button.dispatch('on_release')

    @abstractmethod
    def _from_series(self, word_series):
        pass

    def __next__(self):
        _, word = next(self.dictionary)
        self._last_word = self._from_series(word)
        if Test.EXPERIMENTAL_PRIORITIZE:
            _, word_1 = next(self.dictionary)
            word_1 = self._from_series(word_1)
            self._last_word = WordRecorder.compare(self._last_word, word_1)
        self._clear()
        return self._last_word

    def __iter__(self):
        return self

    @abstractmethod
    def _get_word_for_hint(self) -> str:
        pass

    @abstractmethod
    def get_user_input(self) -> Tuple:
        pass

    @abstractmethod
    def _set_hint(self, hint: str):
        pass

    def hint(self):
        word_for_hint = self._get_word_for_hint()
        left_to_open = []
        for c in word_for_hint.lower():  # Not using set because I want to preserve the order of the letters
            if c not in self._hint_opened and c not in left_to_open:
                left_to_open.append(c)
        chars_count = len(left_to_open)

        for _ in range(min(int(self._hint_chars_to_open), len(left_to_open))):
            self._hint_opened.add(left_to_open.pop(0))

        hint = ""
        for c in word_for_hint:
            hint += (c if c in self._hint_opened or c.lower() in self._hint_opened else '_') + ' '

        if self._hint_chars_to_open < chars_count:
            self._hint_chars_to_open += 0.5

        self.subtract_points(1)
        if "_" not in hint:
            self._earned_points -= 1

        self._set_hint(hint.rstrip())
        self._focus()

    def highlight_red(self, ids):
        for id in ids:
            assert isinstance(self.ids[id], MDTextField), "Only TextFields can be highlighted!"
            self.ids[id].error = True