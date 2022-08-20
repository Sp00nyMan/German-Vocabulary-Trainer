from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField

import TestBuilder


class Footer(MDBoxLayout):
    screen: ObjectProperty(None)


class TextField(MDTextField):
    write_tab = False

    def on_text_validate(self):
        self.parent.parent.ids['footer'].ids['submit'].dispatch('on_release')


class TestScreen(MDScreen):
    NAME = "TEST_SCREEN"

    def __init__(self, test_mode):
        self.__layout = TestBuilder.get_layout(test_mode)
        Builder.load_file(self.__layout)
        super().__init__(name=self.NAME)

        self._test = TestBuilder.get_test(test_mode, self)
        self.ids['footer'].screen = self
        Clock.schedule_once(lambda dt: next(self._test))

    def unload(self):
        Builder.unload_file(self.__layout)

    def get_user_input(self):
        return self._test.get_user_input()

    def on_submit(self, *user_input):
        incorrect_ids = self._test.check(user_input)
        if len(incorrect_ids) == 0:
            self._next_word()
        else:
            self._test.enable_hint_button()
            self.highlight_red(incorrect_ids)

    def _next_word(self):
        try:
            next(self._test)
        except StopIteration:
            self.manager.back()

    def skip(self):
        self._next_word()

    def hint(self):
        self._test.hint()

    def highlight_red(self, ids):
        for id in ids:
            assert isinstance(self.ids[id], MDTextField), "Only TextFields can be highlighted!"
            self.ids[id].error = True
