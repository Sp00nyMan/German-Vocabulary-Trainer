import os
from abc import ABC

from .Tests import NounsTranslate, RegularVerbsTranslate
from .Tests.Test import Test


class TestBuilder(ABC):
    test_layouts = r"GUI\layouts\tests"

    @staticmethod
    def get_test(test_mode: str, test_screen) -> Test:
        match test_mode.lower():
            case "nouns_translate":
                return NounsTranslate(test_screen)
            case "regular_verbs_translate":
                return RegularVerbsTranslate(test_screen)
            case _:
                raise ValueError("Unsupported test mode")

    @staticmethod
    def get_layout(mode: str):
        root_dir = os.getcwd()
        match mode.lower():
            case "nouns_translate":
                return os.path.join(root_dir, TestBuilder.test_layouts, NounsTranslate.LAYOUT_FILE)
            case "regular_verbs_translate":
                return os.path.join(root_dir, TestBuilder.test_layouts, RegularVerbsTranslate.LAYOUT_FILE)