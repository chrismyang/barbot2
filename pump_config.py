


class PumpConfig:
    def __init__(self, pump_config):
        self._pump_config = pump_config

    def get_pump_for_ingredient(self, ingredient_to_find):
        for pump_id,ingredient in self._pump_config.items():
            if ingredient == ingredient_to_find:
                return pump_id

        raise Exception(f"This recipe does not have ingredient '{ingredient}'")
