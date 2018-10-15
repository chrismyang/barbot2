


class PumpConfig:
    def __init__(self, pump_name, enable_pin_number, forward_pin_number, reverse_pin_number):
        self._pump_name = pump_name
        self._enable_pin_number = enable_pin_number
        self._forward_pin_number = forward_pin_number
        self._reverse_pin_number = reverse_pin_number

    def get_pump_name(self):
        return self._pump_name

    def get_enable_pin_number(self):
        return self._enable_pin_number

    def get_forward_pin_number(self):
        return self._forward_pin_number

    def get_reverse_pin_number(self):
        return self._reverse_pin_number
