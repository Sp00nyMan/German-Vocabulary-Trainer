from kivy.core.window import Window
from kivymd.app import MDApp

from GUI.ScreenManager import ScreenManager
from WordRecorder import save_stats

Window.size = (500, 600)


class VocabularyTrainerApp(MDApp):
    def build(self):
        return ScreenManager()

if __name__ == '__main__':
    try:
        VocabularyTrainerApp().run()
    finally:
        save_stats()

