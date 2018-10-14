from driver import Driver
from orchestrator import Orchestrator
from pump_config import PumpConfig
from recipe_library import RecipeLibrary
from recipe import Recipe

# https://www.bonappetit.com/recipe/whiskey-sour
whiskey_sour = Recipe("Whiskey Sour", {
    "bourbon": 2,
    "lemon_juice": 0.75,
    "simple_syrup": 0.75
})

library = RecipeLibrary(whiskey_sour)

driver = Driver()

pump_config = PumpConfig({
    "pump_a": "bourbon",
    "pump_b": "lemon_juice",
    "pump_c": "simple_syrup"
})

orchestrator = Orchestrator()

orchestrator.make_drink(whiskey_sour, pump_config, driver)
