import random

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

    def _party_on_next(self, *args):
        print("party_next", args)
        if not hasattr(self, '_test_screens'):
            raise RuntimeError('Tests were not initialised')
        next_test_id = random.randint(0, len(self._test_screens))
        self.current = TestScreen.NAME + str(next_test_id)

    def _party_test_end(self, *args):
        print(args, self._test_screens)
        # TODO remove test from list

    def load(self, category: str, id: str):
        print(category, id)
        if category.lower() == 'party':
            self._test_screens = []
            for i, test_mode in enumerate(TestBuilder.get_all_tests()):
                test_screen = TestScreen(test_mode, i)
                test_screen.bind(on_next=self._party_on_next)
                test_screen.bind(on_end=self._party_test_end)
                self._test_screens.append(test_screen)
        elif category.lower() in TestBuilder.TEST_MODES:
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
