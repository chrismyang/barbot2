import readline


recipe = readline("What recipe?...")

recipe = RecipeLibrary().look_up_recipe_by_name("whiskey_sour")

Orchestraor().make_drink(recipe, pump_config, driver)