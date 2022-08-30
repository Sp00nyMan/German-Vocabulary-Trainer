from os import path
from typing import Iterable

from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import MDScreen

import TestBuilder


class MainMenuScreen(MDScreen):
    NAME = "MAIN_MENU"
    LAYOUT_PATH = path.join(path.dirname(__file__), r"..\layouts\main_menu.kv")

    def __init__(self, test_mode: str = None):
        Builder.load_file(MainMenuScreen.LAYOUT_PATH)
        super().__init__(name=self.NAME)
        self._load_buttons(test_mode.lower() if test_mode else 'all')

    def unload(self):
        Builder.unload_file(self.LAYOUT_PATH)

    def _load_buttons(self, test_mode):
        if test_mode == 'all':
            modes = list(TestBuilder.TEST_CATEGORIES.keys()) + ['party']
            self._create_buttons(modes)
        elif test_mode in TestBuilder.TEST_CATEGORIES:
            self.ids['back'].disabled = False
            self.ids['back'].opacity = 1
            self.ids['title'].text = test_mode.upper()

            ids = TestBuilder.TEST_CATEGORIES[test_mode]
            titles = map(lambda id: id.split('_')[-1], ids)
            self._create_buttons(titles, ids)
        else:
            raise ValueError(f'Test Mode {test_mode} is not supported :(')

    def _create_buttons(self, titles: Iterable[str], ids: Iterable[str] = None):
        if not ids:
            ids = titles
        for title, id in zip(titles, ids):
            button = MDRectangleFlatButton(text=title.upper(),
                                           id=id,
                                           pos_hint={'center_x': 0.5},
                                           font_size=30)
            button.bind(on_release=self.on_button_clicked)
            self.ids['body'].add_widget(button)

    def on_button_clicked(self, sender: MDRectangleFlatButton):
        self.manager.load(sender.text, sender.id)
