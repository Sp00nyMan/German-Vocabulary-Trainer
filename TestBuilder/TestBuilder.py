import os

from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from Entities import Word
from .Tests import NounsTranslate


class TestBuilder:
    test_layouts = r"GUI\layouts\tests"

    def __init__(self, mode: str, test_screen: MDScreen):
        match mode.lower():
            case "nouns_translate":
                self._test = NounsTranslate(test_screen)
            case _:
                raise ValueError("Unsupported mode")

    @staticmethod
    def get_layout(mode: str):
        root_dir = os.getcwd()
        match mode.lower():
            case "nouns_translate":
                return os.path.join(root_dir, TestBuilder.test_layouts, NounsTranslate.LAYOUT_FILE)

    def check(self, guess):
        return self._test.check(guess)

    def hint(self):
        self._test.hint()

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._test)

    def get_user_input(self):
        return self._test.get_user_input()
