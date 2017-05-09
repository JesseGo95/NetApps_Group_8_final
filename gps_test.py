import serial
import json
import time

port = serial.Serial("/dev/ttyUSB0", 9600)

port.write("$PMTK220,5000*1B\r\n".encode())
port.write("$PMTK300,5000,0,0,0,0*18\r\n".encode())
port.write("$PMTK314,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0*29\r\n".encode())
while True:
    x = port.readline()
    x = x.decode().strip()
    #data = json.loads(x.decode())
    #print(x)
    try:
        time.sleep(1)
        #data = json.loads(x)
        print(x)
    except:
        print("Cannot parse data")

