import readline

from recipe_library import RecipeLibrary
from recipe import Recipe


# Hi jason!
#greetings!

def print_recipes(library):
    for recipe in library.get_recipes():


# https://www.bonappetit.com/recipe/whiskey-sour
whiskey_sour = Recipe(
    {
        "bourbon": 2,
        "lemon_juice": 0.75,
        "simple_syrup": 0.75
    }
)

library = RecipeLibrary()

print_recipes(library)


recipe = readline.("What recipe?...")

recipe = RecipeLibrary().look_up_recipe_by_name("whiskey_sour")

Orchestraor().make_drink(recipe, pump_config, driver)