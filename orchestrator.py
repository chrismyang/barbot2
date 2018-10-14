



class Orchestrator:




    def make_drink(self, recipe, pump_config, driver):

       for (ingredient, amount) in recipe.get_ingredients():
           pump = pump_config.get_pump_for_ingredient(ingredient)
           driver.dispense(pump, amount)
