from kivy.uix.screenmanager import ScreenManager as SM
from kivymd.uix.screen import MDScreen

from GUI.screens.MainMenuScreen import MainMenuScreen
from GUI.screens.TestScreen import TestScreen


class ScreenManager(SM):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.main_menu_screen: MDScreen = MainMenuScreen()
        self.add_widget(self.main_menu_screen)

        self.current = MainMenuScreen.NAME

        self.test_screen: TestScreen = None

    def load(self, category: str):
        match category.lower():
            case "substantive":
                mode = "nouns_translate"
            case _:
                return

        self._reload_test_screen(mode)
        self.current = TestScreen.NAME

    def _reload_test_screen(self, test_mode):
        if self.test_screen:
            self.remove_widget(self.get_screen(self.test_screen.name))
        self.test_screen = TestScreen(test_mode)
        self.add_widget(self.test_screen)

    def back(self):
        self.current = MainMenuScreen.NAME

    def skip(self):
        self.test_screen.skip()
