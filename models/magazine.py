# models/magazine.py

class Magazine:
    def __init__(self, name=None, category=None):
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:  # Check if value is a non-empty string
            raise ValueError("Category must be a non-empty string")
        self._category = value
