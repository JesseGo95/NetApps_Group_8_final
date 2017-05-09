import serial
import json
import time
from datetime import datetime
#from pytz import timezone

#tz = timezone('EST')

port = serial.Serial("/dev/ttyUSB0", 9600)
xbee = serial.Serial("/dev/ttyUSB1", 9600)

data = {"time":0}
data["lat"]=0
data["long"]=-0

port.write("$PMTK220,5000*1B\r\n".encode())
port.write("$PMTK300,5000,0,0,0,0*18\r\n".encode())
port.write("$PMTK314,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0*29\r\n".encode())
while True:
    x = port.readline()
    x = x.decode().strip()
    line = x.split(",")
    data["time"] = time.strftime("%b %d %Y %H:%M:%S", datetime.utcnow().timetuple())
    try:
        lat = float(line[3])/100
        lon = float(line[5])/100
    except:
        print ("ERROR: invalid data")
        string = json.dumps(data)+"\n"
        xbee.write(string.encode())
        print(data)
        continue
    if line[4] == "S":
        lat = lat * -1
    if line[6] == "W":
        lon = lon * -1
    data["lat"] = lat
    data["long"] = lon
    print(data)
    string = json.dumps(data)+"\n"
    xbee.write(string.encode())
    #data = json.loads(x.decode())
    #print(x)
    #try:
    #    time.sleep(1)
        #data = json.loads(x)
    #    print(x)
    #except:
    #    print("Cannot parse data")

