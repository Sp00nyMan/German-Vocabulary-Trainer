from kivy.core.window import Window
from kivymd.app import MDApp

from GUI.ScreenManager import ScreenManager

Window.size = (500, 600)

class VocabulayTrainerApp(MDApp):
    def build(self):
        return ScreenManager()

if __name__ == '__main__':
    VocabulayTrainerApp().run()