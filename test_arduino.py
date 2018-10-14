from arduino import Arduino
import time

b = Arduino('/dev/tty.usbmodem14411')
pin = 9

#declare output pins as a list/tuple
b.output([pin])

for x in range(10):
    b.setHigh(pin)
    time.sleep(1)
    print(b.getState(pin))
    b.setLow(pin)
    print(b.getState(pin))
    time.sleep(1)

b.close()