import time

from arduino import Arduino


class SimpleArduinoDriver:
    def __init__(self, arduino_device_path, pump_configs, flow_rate):
        self._arduino = Arduino(arduino_device_path)
        self._pump_configs = pump_configs
        self._flow_rate = flow_rate

        output_pins = []

        for config in self._pump_configs:
            output_pins.append(config.get_enable_pin_number())
            output_pins.append(config.get_forward_pin_number())
            output_pins.append(config.get_reverse_pin_number())

        self._arduino.output(output_pins)

    def start_prime(self, pump_name):
        self._prime_start = time.time()

        pump_config = self._find_config(pump_name)

        self._arduino.setHigh(pump_config.get_enable_pin_number())
        self._arduino.setHigh(pump_config.get_forward_pin_number())

    def end_prime(self, pump_name):
        pump_config = self._find_config(pump_name)

        self._arduino.setLow(pump_config.get_enable_pin_number())
        self._arduino.setLow(pump_config.get_forward_pin_number())

        now = time.time()

        return now - self._prime_start

    def start_purge(self, pump_name):
        pump_config = self._find_config(pump_name)

        self._arduino.setHigh(pump_config.get_enable_pin_number())
        self._arduino.setHigh(pump_config.get_reverse_pin_number())

    def end_purge(self, pump_name):
        pump_config = self._find_config(pump_name)

        self._arduino.setLow(pump_config.get_enable_pin_number())
        self._arduino.setLow(pump_config.get_reverse_pin_number())

    def dispense(self, pump_name, amount_to_dispense):
        pump_config = self._find_config(pump_name)

        time_to_leave_on = amount_to_dispense / self._flow_rate

        print(f"[SimpleArduinoDriver] Enabling pump '{pump_name}' for {time_to_leave_on} s")

        self._arduino.setHigh(pump_config.get_enable_pin_number())
        self._arduino.setHigh(pump_config.get_forward_pin_number())

        time.sleep(time_to_leave_on)

        self._arduino.setLow(pump_config.get_enable_pin_number())
        self._arduino.setLow(pump_config.get_forward_pin_number())

    def close(self):
        self._arduino.close()

    def _find_config(self, pump_name):
        for pump_config in self._pump_configs:
            if pump_config.get_pump_name() == pump_name:
                return pump_config

        raise Exception(f"Cannot find pump with name '{pump_name}'")
