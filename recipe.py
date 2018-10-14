


class Recipe:
    def __init__(self, name, ingredients):
        self._name = name
        self._ingredients = ingredients

    def get_name(self):
        return self._name

    def get_ingredients(self):
        return self._ingredients.items()
