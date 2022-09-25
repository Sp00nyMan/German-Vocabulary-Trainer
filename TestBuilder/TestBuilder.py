from typing import List

import pandas as pd

from .Tests import NounsTranslate, VerbsTranslate, AdjectivesTranslate, AdverbsTranslate, \
    NounsPlural, NounsGenus, VerbsKonjugate, Test, Phrases


class TestMode:
    def __init__(self, id: str, cls: Test, category: str, name: str):
        self.id = id
        self.cls = cls
        self.category = category
        self.name = name

    def __eq__(self, other):
        return self.id == other or self.cls == other

    def __str__(self):
        return f"{self.id} {self.cls} {self.category} {self.name}"

    @classmethod
    def from_series(cls, series: pd.Series):
        return cls(series['id'], series["class"], series['category'], series['name'])

    @classmethod
    def from_dataframe(cls, dataframe: pd.DataFrame) -> List:
        return [TestMode.from_series(series) for _, series in dataframe.iterrows()]


TESTS = pd.DataFrame(data=[["nouns_übersetzen", NounsTranslate, "substantive", "Nouns Übersetzen"],
                           ["nouns_plural", NounsPlural, "substantive", "Nouns Plural"],
                           ["nouns_genus", NounsGenus, "substantive", "Nouns Genus"],
                           ["verbs_übersetzen", VerbsTranslate, "verben", "Verbs Übersetzen"],
                           ["verbs_konjugate", VerbsKonjugate, "verben", "Verbs Konjugate"],
                           ["adjectives_übersetzen", AdjectivesTranslate, "adjektive", "Adjektive Übersetzen"],
                           ["adverbs_übersetzen", AdverbsTranslate, "adverben", "Adverben Übersetzen"],
                           ["phrases", Phrases, None, "Phrases"]],
                     columns=["id", "class", "category", "name"])

TEST_LAYOUTS_PATH = r"GUI\layouts\tests"


def get_all_tests() -> List[TestMode]:
    return TestMode.from_dataframe(TESTS)


def get_test_groups() -> List[str]:
    groups = TESTS.category.dropna().unique().tolist()
    return groups


def get_independent_modes() -> List[TestMode]:
    independent = TestMode.from_dataframe(TESTS[TESTS.category.isna()])
    return independent


def get_by_category(category: str) -> List[TestMode]:
    category = TestMode.from_dataframe(TESTS[TESTS.category == category])
    return category


def check_test_mode(test_mode):
    if test_mode not in get_all_tests():
        raise ValueError(f"Unsupported Test Mode {test_mode}")


def _get_test_class(test_mode: str) -> Test.__class__:
    test = TESTS[TESTS.id == test_mode]
    if len(test) != 1:
        raise NotImplementedError(f"Unsupported Test Mode {test_mode}")
    return test.iloc[0]["class"]


def get_test_mode(test_class: Test) -> str:
    test = TESTS.where(TESTS["class"] == test_class)
    if len(test) != 1:
        raise NotImplementedError(f"Unsupported Test: {test_class}")
    return test[0].id


def get_test(test_mode: str, test_screen) -> Test:
    check_test_mode(test_mode)
    return _get_test_class(test_mode)(test_screen.ids['footer'])
