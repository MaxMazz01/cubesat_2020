# cubesat_2020_testing
Some code I am testing for BWSI 2020. Mostly code to run Bluetooth connection between Raspberry Pi and students' computers.

WPA_SUPPLICANT_EXAMPLE can be modified with your network name and password. Save this modified file as "wpa_supplicant.conf" in the boot folder on your Pi's SD card. Now, the Pi should automatically connect to the network you specified in the file when it boots.

test_tx.py and test_rx.py just send text over a serial connection.

creating\_bluetooth\_connection.txt and establishing\_rfcomm\_port.txt are instructions for creating a virtual serial port over bluetooth.
