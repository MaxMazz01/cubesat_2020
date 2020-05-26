import serial
import time

while True:
    try:
        radio = serial.Serial('/dev/rfcomm0', 9600)
        print(radio.name)
    except serial.serialutil.SerialException:
        print("couldn't open port")
    while True:
        try:
            radio.write(b'testing...\n')
            print('testing...\n')
            time.sleep(1)
        except serial.serialutil.SerialException:
            print("serial send failed")
            radio.close()
            pass
