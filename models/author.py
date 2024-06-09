# models/author.py

class Author:
    def __init__(self, name=None):
        self._name = name  # Use the private attribute _name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):  # Check if _name attribute exists
            raise AttributeError("Cannot change author's name after instantiation")
        self._name = value
