from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField

from TestBuilder import TestBuilder


class Footer(MDAnchorLayout):
    screen: ObjectProperty(None)


class TextField(MDTextField):
    write_tab = False

    def on_text_validate(self):
        self.parent.parent.ids['footer'].ids['submit'].dispatch('on_release')


class TestScreen(MDScreen):
    NAME = "TEST_SCREEN"

    def __init__(self, test_mode):
        layout = TestBuilder.get_layout(test_mode)
        Builder.unload_file(layout)
        Builder.load_file(layout)
        super().__init__(name=self.NAME)

        self._test = TestBuilder.get_test(test_mode, self)
        self.ids['footer'].screen = self
        Clock.schedule_once(lambda dt: next(self._test))

    def get_user_input(self):
        return self._test.get_user_input()

    def on_submit(self, *user_input):
        incorrect_ids = self._test.check(user_input)
        if len(incorrect_ids) == 0:
            next(self._test)
        else:
            self._test.enable_hint_button()
            self.highlight_red(incorrect_ids)

    def skip(self):
        self._next_word()

    def hint(self):
        self._test.hint()

    def highlight_red(self, ids):
        for id in ids:
            assert isinstance(self.ids[id], MDTextField), "Only TextFields can be highlighted!"
            self.ids[id].error = True
