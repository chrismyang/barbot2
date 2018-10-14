

class Orchestrator:
    def make_drink(self, recipe, pump_config, driver):
        print(f"Making drink '{recipe.get_name()}'...")

        for ingredient, amount in recipe.get_ingredients():
            pump = pump_config.get_pump_for_ingredient(ingredient)

            print(f"  - Dispensing {amount} oz(s) of '{ingredient}' from pump '{pump}'...", end=" ")
            driver.dispense(pump, amount)
            print("done")

