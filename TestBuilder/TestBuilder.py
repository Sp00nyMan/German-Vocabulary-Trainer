import os
from abc import ABC

from .Tests import NounsTranslate, RegularVerbsTranslate
from .Tests.Test import Test

TEST_MODES = {'substantive':
                  ['nouns_übersetzen',
                   'nouns_plural',  # TODO
                   'nouns_genus'],  # TODO
              'regelmässig verben':
                  ['regular_verbs_übersetzen',
                   'regular_verbs_konjugate'],  # TODO
              'unregelmässig verben':
                  ['irregular_verbs_übersetzen',  # TODO
                   'irregular_verbs_konjugate',  # TODO
                   'irregular_verbs_präteritum',  # TODO
                   'irregular_verbs_perfekt'],  # TODO
              'adjektive':
                  ['adjectives_übersetzen'],  # TODO
              'adverben':
                  ['adverbs_übersetzen']  # TODO
              }


def check_test_mode(test_mode):
    if not any([test_mode in modes for modes in TEST_MODES.values()]):
        raise ValueError(f"Unsupported Test Mode {test_mode}")


class TestBuilder(ABC):
    test_layouts = r"GUI\layouts\tests"

    @staticmethod
    def _get_test_class(test_mode: str) -> Test.__class__:
        match test_mode.lower():
            case "nouns_übersetzen":
                return NounsTranslate
            case "regular_verbs_übersetzen":
                return RegularVerbsTranslate

    @staticmethod
    def get_test(test_mode: str, test_screen) -> Test:
        check_test_mode(test_mode)
        return TestBuilder._get_test_class(test_mode)(test_screen)

    @staticmethod
    def get_layout(test_mode: str):
        check_test_mode(test_mode)
        root_dir = os.getcwd()
        layout_file = TestBuilder._get_test_class(test_mode).LAYOUT_FILE
        return os.path.join(root_dir, TestBuilder.test_layouts, layout_file)
