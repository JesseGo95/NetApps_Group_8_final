import serial
import json

port = serial.Serial("/dev/ttyUSB0", 9600)

while True:
	x = port.readline()
	x = x.decode().strip()
	#data = json.loads(x.decode())
	#print(x)
	try:
		data = json.loads(x)
		print(data)
	except:
		print("Cannot parse data")
