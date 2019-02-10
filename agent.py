
from arduino_driver import SimpleArduinoDriver
from pump_config import PumpConfig

from socketIO_client import SocketIO

class BarbotCentralListener:

    def __init__(self, url):
        parts = url.rsplit(":", 1)
        host = parts[0]
        port = int(parts[1])

        self._socketIO = SocketIO(host, port, verify=False)
        self._socketIO.on('connect', self._on_connect)

    def _on_connect(self):
        self._socketIO.emit()
        print('welcome received')

    def set_purge_command_listener(self, on_purge_command):
        pass

    def set_prime_command_listener(self, on_prime_command_start, on_prime_command_stop):
        self._socketIO.on('prime_start', on_prime_command_start)
        self._socketIO.on('prime_stop', on_prime_command_stop)

    def set_make_drink_command_listener(self, on_make_drink_command):
        pass

    def run(self):
        self._socketIO.wait()


if __name__ == '__main__':

    # arduino_device_path = "/dev/cu.usbmodem14111"
    #
    # driver = SimpleArduinoDriver(
    #     arduino_device_path,
    #     [
    #         PumpConfig("P1", enable_pin_number=12, forward_pin_number=51, reverse_pin_number=50),
    #         PumpConfig("P2", enable_pin_number=10, forward_pin_number=49, reverse_pin_number=48),
    #         PumpConfig("P3", enable_pin_number=8, forward_pin_number=44, reverse_pin_number=45),
    #         PumpConfig("P4", enable_pin_number=7, forward_pin_number=43, reverse_pin_number=42),
    #         PumpConfig("P5", enable_pin_number=9, forward_pin_number=47, reverse_pin_number=46)
    #     ],
    #     flow_rate=0.2213762726  # oz/sec
    # )

    driver = None

    url = "http://localhost:5000"

    print(f"Connecting to BarbotCentral at '{url}'...")
    listener = BarbotCentralListener(url)

    def on_prime_command_start(pump_to_prime):
        print(f"Received command 'start priming' '{pump_to_prime}'...")
        # driver.start_prime(pump_to_prime)

    def on_prime_command_end(pump_to_prime):
        print(f"Received command 'stop priming' '{pump_to_prime}'...")
        # driver.end_prime(pump_to_prime)

    listener.set_prime_command_listener(on_prime_command_start, on_prime_command_end)

    print(f"Connected successfully. Waiting for commands...")
    listener.run()