import sys

from arduino_driver import SimpleArduinoDriver
from driver import Driver
from orchestrator import Orchestrator
from ingredient_layout import IngredientLayout
from pump_config import PumpConfig
from recipe_library import RecipeLibrary
from recipe import Recipe
import serial.tools.list_ports

# https://www.bonappetit.com/recipe/whiskey-sour
whiskey_sour = Recipe("Whiskey Sour", {
    "bourbon": 2,
    "lemon_juice": 0.75,
#    "simple_syrup": 0.75
})

library = RecipeLibrary(whiskey_sour)


ports = list(serial.tools.list_ports.comports())
print("Select the port that the Arduino is connected on")
print("=" * 80)
for i in range(len(ports)):
    port = ports[i]
    print(f"({i}) {port.device} {port.description} {port.manufacturer}")

selection = int(input("Type in a number from the choices above: "))

# arduino_device_path = "/dev/cu.usbmodem14111"

arduino_device_path = ports[selection].device

driver = SimpleArduinoDriver(
    arduino_device_path,
    [
        PumpConfig("P1", enable_pin_number=12, forward_pin_number=51, reverse_pin_number=50),
        PumpConfig("P2", enable_pin_number=10, forward_pin_number=49, reverse_pin_number=48),
        PumpConfig("P3", enable_pin_number=8, forward_pin_number=44, reverse_pin_number=45),
        PumpConfig("P4", enable_pin_number=7, forward_pin_number=43, reverse_pin_number=42),
        PumpConfig("P5", enable_pin_number=9, forward_pin_number=47, reverse_pin_number=46)
    ],
    flow_rate=0.2213762726 # oz/sec
)

ingredient_layout = IngredientLayout({
    "P2": "bourbon",
    "P3": "lemon_juice",
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

    elif command == "prime":
        pump_to_prime = sys.argv[2]

        input(f'Hit enter to begin prime of pump {pump_to_prime}:')
        print(f"Prime pump '{pump_to_prime}'...")
        driver.start_prime(pump_to_prime)

        input('Hit enter to stop prime')
        driver.end_prime(pump_to_prime)

        driver.close()

    elif command == "make_drink":
        print("Make Drink")
        print("==========")
        print()

        # recipe_name = sys.argv[2]

        orchestrator = Orchestrator()
        orchestrator.make_drink(whiskey_sour, ingredient_layout, driver)
        driver.close()


