import serial
import time
import json

port = serial.Serial("/dev/ttyUSB0", 9600)

data = {"count":0}
data["lat"]=37.229573
data["lon"]=-80.413939

while True:
	string = json.dumps(data)+"\n"
	port.write(string.encode())
	data["count"]+=1
	time.sleep(1)
