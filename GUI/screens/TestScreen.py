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

        self.test_builder = TestBuilder(test_mode, self)
        self.ids['footer'].screen = self
        Clock.schedule_once(lambda dt: self._next_word())

    def get_user_input(self):
        return self.test_builder.get_user_input()

    def on_submit(self, *user_input):
        if self.test_builder.check(user_input):
            self._next_word()
        else:
            self._wrong()

    def _next_word(self):
        self.last_word = next(self.test_builder)

    def _wrong(self):
        self.ids['footer'].ids['hint'].disabled = False
        self.ids['footer'].ids['hint'].opacity = 1

    def skip(self):
        self._next_word()

    def hint(self):
        self.test_builder.hint()

