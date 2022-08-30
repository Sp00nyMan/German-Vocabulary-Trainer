import os

from .Tests import NounsTranslate, VerbsTranslate, AdjectivesTranslate, AdverbsTranslate, NounsPlural, NounsGenus, Test

TEST_LAYOUTS_PATH = r"GUI\layouts\tests"
TEST_CATEGORIES = {'substantive':
                       ['nouns_übersetzen',
                        'nouns_plural',
                        'nouns_genus'],
                   'verben':
                       ['verbs_übersetzen',
                        # 'verbs_konjugate',  # TODO
                        # 'verbs_präteritum',  # TODO
                        # 'verbs_perfekt',  # TODO
                        # 'verbs_partizip II',  # TODO
                        ],
                   'adjektive':
                       ['adjectives_übersetzen',
                        # 'adjectives_compare',  # TODO
                        ],
                   'adverben':
                       ['adverbs_übersetzen'],
                   }


def get_all_tests():
    tests = []
    for modes in TEST_CATEGORIES.values():
        tests += modes
    return tests


def check_test_mode(test_mode):
    if test_mode not in get_all_tests():
        raise ValueError(f"Unsupported Test Mode {test_mode}")


def _get_test_class(test_mode: str) -> Test.__class__:
    match test_mode.lower():
        case "nouns_übersetzen":
            return NounsTranslate
        case "nouns_plural":
            return NounsPlural
        case "nouns_genus":
            return NounsGenus
        case "verbs_übersetzen":
            return VerbsTranslate
        case "adjectives_übersetzen":
            return AdjectivesTranslate
        case "adverbs_übersetzen":
            return AdverbsTranslate
        case _:
            raise NotImplementedError(f"Unsupported Test Mode {test_mode}")


def get_test(test_mode: str, test_screen) -> Test:
    check_test_mode(test_mode)
    return _get_test_class(test_mode)(test_screen.ids['footer'])
