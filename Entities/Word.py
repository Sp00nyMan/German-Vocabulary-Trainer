class Word:
    def __init__(self, translation: str, comparison_function=None):
        self._translation = translation.strip().lower()
        if comparison_function:
            self.__eq__ = comparison_function

    def __str__(self):
        pass

    @property
    def translation(self):
        return self._translation
