from kivy.uix.screenmanager import ScreenManager as SM
from kivymd.uix.screen import MDScreen

import TestBuilder
from GUI.screens.MainMenuScreen import MainMenuScreen
from GUI.screens.TestScreen import TestScreen


class ScreenManager(SM):
    main_menu_screen: MainMenuScreen = None
    test_screen: TestScreen = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._load_main_menu(None)
        self.current = MainMenuScreen.NAME

    def load(self, category: str, id: str):
        print(category, id)
        if category.lower() in TestBuilder.TEST_MODES:
            self._load_main_menu(id)
            self.current = MainMenuScreen.NAME
        else:
            self._load_test_screen(id)
            self.current = TestScreen.NAME

    def _load_test_screen(self, test_mode):
        if self.test_screen:
            self.test_screen.unload()
            self.remove_widget(self.test_screen)
        self.test_screen = TestScreen(test_mode)
        self.add_widget(self.test_screen)

    def _load_main_menu(self, category):
        if self.main_menu_screen:
            self.main_menu_screen.unload()
            self.remove_widget(self.main_menu_screen)
        self.main_menu_screen = MainMenuScreen(category)
        self.add_widget(self.main_menu_screen)

    def back(self):
        if self.current == MainMenuScreen.NAME:
            self._load_main_menu(None)
        self.current = MainMenuScreen.NAME

    def skip(self):
        self.test_screen.skip()
