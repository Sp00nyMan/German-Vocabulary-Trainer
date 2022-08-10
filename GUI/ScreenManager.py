import os.path

from kivy.uix.screenmanager import ScreenManager as SM
from kivymd.uix.screen import MDScreen

import TestBuilder.TestBuilder
from GUI.screens.MainMenuScreen import MainMenuScreen
from GUI.screens.TestScreen import TestScreen


class ScreenManager(SM):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.main_menu_screen: MDScreen = MainMenuScreen()
        self.add_widget(self.main_menu_screen)

        self.current = MainMenuScreen.NAME

        self.test_screen: MDScreen = None

    def load(self, category: str):
        cwd = os.path.dirname(__file__)
        match category.lower():
            case "substantive":
                test_layout_file = r"layouts\tests\nouns_translate.kv"
                test_layout_file = os.path.join(cwd, test_layout_file)
                mode = "nouns_translate"
            case _:
                return

        self._reload_test_screen(test_layout_file, mode)
        self.current = TestScreen.NAME
        print('test_loaded')

    def _reload_test_screen(self, test_layout, test_mode):
        if self.test_screen:
            self.remove_widget(self.get_screen(self.test_screen.name))
        self.test_screen = TestScreen(test_layout, test_mode)
        self.add_widget(self.test_screen)

    def back(self):
        self.current = MainMenuScreen.NAME
