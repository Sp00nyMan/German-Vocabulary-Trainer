from kivy.uix.screenmanager import ScreenManager as SM

from GUI.screens.MainMenuScreen import MainMenuScreen


class ScreenManager(SM):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.main_menu_screen = MainMenuScreen()
        self.add_widget(self.main_menu_screen)

        self.current = MainMenuScreen.NAME

    def load(self, category):
        print(category)

    def back(self):
        print("BACK")