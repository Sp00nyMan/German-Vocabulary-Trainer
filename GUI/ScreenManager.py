import random

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager as KivySM

import TestBuilder
from GUI.screens.MainMenuScreen import MainMenuScreen
from GUI.screens.TestScreen import TestScreen


class ScreenManager(KivySM):
    main_menu_screen: MainMenuScreen = None
    test_screen: TestScreen = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_file(r'GUI/layouts/test_screen.kv')
        self._reload_main_menu(None)
        self.current = MainMenuScreen.NAME

    def _party_load(self):
        self._party_tests = []
        self.test_screen.bind(on_next=self._party_on_next,
                              on_end=self._party_test_end)
        for test in TestBuilder.get_all_tests():
            self._party_tests.append(TestBuilder.get_test(test, self.test_screen))
        self._party_on_next()

    def _party_on_next(self, *args):
        if not hasattr(self, '_party_tests'):
            raise RuntimeError('Tests were not initialised')
        next_test = random.sample(self._party_tests, 1)[0]
        self.test_screen.load(next_test)
        return True

    def _party_test_end(self, sender):
        test = sender._test
        print(f"Congratulations! You finished the test: {test}")
        self._party_tests.remove(test)
        if len(self._party_tests) != 0:
            self._party_on_next()
            return True
        else:
            return False

    def load(self, category: str, test_id: str):
        print(category, test_id)
        if category.lower() == 'party':
            self._reload_test_screen()
            self._party_load()
            self.current = TestScreen.NAME
        elif category.lower() in TestBuilder.TEST_CATEGORIES:
            self._reload_main_menu(test_id)
            self.current = MainMenuScreen.NAME
        else:
            self._reload_test_screen()
            self.test_screen.load(TestBuilder.get_test(test_id, self.test_screen))
            self.current = TestScreen.NAME

    def _reload_test_screen(self):
        if self.test_screen:
            self.test_screen.kill()
            self.remove_widget(self.test_screen)
        self.test_screen = TestScreen()
        self.add_widget(self.test_screen)

    def _reload_main_menu(self, category):
        if self.main_menu_screen:
            self.main_menu_screen.unload()
            self.remove_widget(self.main_menu_screen)
        self.main_menu_screen = MainMenuScreen(category)
        self.add_widget(self.main_menu_screen)

    def back(self):
        if self.current == MainMenuScreen.NAME:
            self._reload_main_menu(None)
        self.current = MainMenuScreen.NAME

    def skip(self):
        self.test_screen.skip()
