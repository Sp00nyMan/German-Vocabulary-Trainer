from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField

import DataLoader


class Footer(MDBoxLayout):
    screen: ObjectProperty(None)


class TextField(MDTextField):
    write_tab = False

    def on_text_validate(self):
        self.parent.submit()


class TestScreen(MDScreen):
    NAME = "TEST_SCREEN"

    def __init__(self):
        super().__init__(name=self.NAME)

        self.register_event_type('on_next')
        self.register_event_type('on_done')

        self.ids['footer'].screen = self

        self._test = None

    def load(self, test):
        if self._test is not None:
            self.remove_widget(self._test)
            self._test = None
        self._test = test
        self.add_widget(self._test)
        Clock.schedule_once(lambda dt: self.on_next())

    def kill(self):
        """
        Unloads Test's layout file
        """
        self._test.unload()

    def get_user_input(self):
        return self._test.get_user_input()

    def on_submit(self, *user_input):
        incorrect_ids = self._test.check(user_input)
        if len(incorrect_ids) == 0:
            self.dispatch('on_next')
        else:
            self._test.enable_hint_button()
            self._test.highlight_red(incorrect_ids)

    def skip(self):
        DataLoader.update_record(self._test, -1)
        self.dispatch('on_next')

    def hint(self):
        self._test.hint()

    def on_next(self):
        try:
            next(self._test)
            DataLoader.update_record(self._test)
        except StopIteration:
            self.dispatch('on_done')

    def on_done(self):
        self.parent.back()
