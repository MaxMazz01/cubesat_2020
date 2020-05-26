import serial

radio = serial.Serial('/dev/rfcomm0', 9600)
print(radio.name)
while True:
    print(radio.read())
