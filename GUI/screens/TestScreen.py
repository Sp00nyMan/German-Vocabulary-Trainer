from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from Entities import Word
from TestBuilder import TestBuilder


class TestScreen(MDScreen):
    NAME = "TEST_SCREEN"

    def __init__(self, layout_file, test_mode):
        Builder.load_file(layout_file)
        super().__init__(name=self.NAME)

        self.test_builder = TestBuilder(self, test_mode)
        self.last_word: Word = next(self.test_builder)

    def on_submit(self, *args):
        print(args)
        print(self.last_word == args)
        self.last_word = next(self.test_builder)
        self.test_builder.update_screen(self, self.last_word)
