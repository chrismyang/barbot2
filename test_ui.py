import sys

from arduino_driver import SimpleArduinoDriver
from driver import Driver
from orchestrator import Orchestrator
from ingredient_layout import IngredientLayout
from pump_config import PumpConfig
from recipe_library import RecipeLibrary
from recipe import Recipe

# https://www.bonappetit.com/recipe/whiskey-sour
whiskey_sour = Recipe("Whiskey Sour", {
    "bourbon": 2,
    "lemon_juice": 0.75,
#    "simple_syrup": 0.75
})

library = RecipeLibrary(whiskey_sour)

driver = SimpleArduinoDriver(
    "/dev/tty.usbmodem14411",
    [
        PumpConfig("pump_a", enable_pin_number=4, forward_pin_number=2, reverse_pin_number=3),
        PumpConfig("pump_b", enable_pin_number=13, forward_pin_number=11, reverse_pin_number=12)
    ],
    flow_rate=0.2213762726 # oz/sec
)

ingredient_layout = IngredientLayout({
    "pump_a": "bourbon",
    "pump_b": "lemon_juice",
    "pump_c": "simple_syrup"
})

if __name__ == "__main__":
    command = sys.argv[1]

    if command == "calibrate":
        print("Calibrate Barbot")
        print("================")
        print()

        pump_to_calibrate = sys.argv[2]

        input('Hit enter to begin calibration')
        driver.start_prime(pump_to_calibrate)

        input('Hit enter to stop calibration.')
        duration = driver.end_prime(pump_to_calibrate)

        print(f"Ran for {duration} s.  Compute (amount_pumped)/{duration} for the flow rate.")

        driver.close()
    elif command == "purge":
        pump_to_purge = sys.argv[2]

        input(f'Hit enter to begin purge of pump {pump_to_purge}:')
        print(f"Purging pump '{pump_to_purge}'...")
        driver.start_purge(pump_to_purge)

        input('Hit enter to stop purge')
        driver.end_purge(pump_to_purge)

        driver.close()

    elif command == "make_drink":
        print("Make Drink")
        print("==========")
        print()

        # recipe_name = sys.argv[2]

        orchestrator = Orchestrator()
        orchestrator.make_drink(whiskey_sour, ingredient_layout, driver)
        driver.close()


