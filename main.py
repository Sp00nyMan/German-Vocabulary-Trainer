from kivy.core.window import Window
from kivymd.app import MDApp

import DataLoader
from GUI.ScreenManager import ScreenManager

Window.size = (500, 600)


class VocabularyTrainerApp(MDApp):
    def build(self):
        return ScreenManager()

if __name__ == '__main__':
    try:
        VocabularyTrainerApp().run()
    finally:
        DataLoader.save_stats()

