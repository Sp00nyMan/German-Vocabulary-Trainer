from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import MDScreen

import DataLoader


class MainMenuScreen(MDScreen):
    NAME = "MAIN_MENU"
    def __init__(self):
        Builder.load_file("E:\My Drive\Deutsch\Vocabulary Trainer\GUI\layouts\main_menu.kv")
        super().__init__(name=self.NAME)
        self._load_buttons()

    def _load_buttons(self):
        for category in DataLoader.sheet_names:
            button = MDRectangleFlatButton(text=category.upper())
            button.bind(on_release=self.on_button_clicked)
            self.ids['body'].add_widget(button)

    def on_button_clicked(self, sender:MDRectangleFlatButton):
        self.manager.load(sender.text)