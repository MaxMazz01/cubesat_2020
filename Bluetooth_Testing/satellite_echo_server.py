#code from http://www.python-exemplary.com/index_en.php?inhalt_links=navigation_en.inc.php&inhalt_mitte=raspi/en/bluetooth.inc.php

from btpycom import *

def onStateChanged(state, msg):
    if state == "LISTENING":
        print("Server is listening")
    elif state == "CONNECTED":
        print("Connection established to", msg)
    elif state == "MESSAGE":
        print("Got message", msg)
        server.sendMessage(msg)
       
serviceName = "EchoServer"
server = BTServer(serviceName, stateChanged = onStateChanged)
