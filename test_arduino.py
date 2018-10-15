from arduino import Arduino
import time

b = Arduino('/dev/tty.usbmodem14411')
pin = 9

#declare output pins as a list/tuple
b.output([11, 12, 13])

pins = [12, 13]

for x in range(10):
    for pin in pins:
        b.setHigh(pin)
        print(f"pin {pin} state: {b.getState(pin)}")

    time.sleep(2)

    for pin in pins:
        b.setLow(pin)
        print(f"pin {pin} state: {b.getState(pin)}")

    # time.sleep(1)

    s = input('--> ')

    if s == "exit":
        break

b.close()
