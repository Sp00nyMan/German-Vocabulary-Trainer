from os import path

from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import MDScreen

import DataLoader


class MainMenuScreen(MDScreen):
    NAME = "MAIN_MENU"

    def __init__(self):
        p = path.join(path.dirname(__file__), r"..\layouts\main_menu.kv")
        Builder.load_file(p)
        super().__init__(name=self.NAME)
        self._load_buttons()

    def _load_buttons(self):
        for category in DataLoader.sheet_names:
            button = MDRectangleFlatButton(text=category.upper(),
                                           pos_hint={'center_x': 0.5},
                                           font_size=30)
            button.bind(on_release=self.on_button_clicked)
            self.ids['body'].add_widget(button)

    def on_button_clicked(self, sender:MDRectangleFlatButton):
        self.manager.load(sender.text)