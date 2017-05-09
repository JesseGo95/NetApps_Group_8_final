import pymongo
from pymongo import MongoClient
import serial
import json
port = serial.Serial("/dev/ttyUSB0", 9600)

client = MongoClient('localhost')
db = client.test_database
collection = db.test_collection

while True:
    line = port.readline()
    line = line.decode().strip()
    try: 
        data = json.loads(line)
        lat = data["lat"]
        long = data["long"]
        settime = data["time"]
        if (lat!=0 and long!=0):
            #collection.remove({})
            post= {}
            post = {"lat" :lat, "long" :long,"time":settime}
            post_id = collection.insert_one(post)
            print(data)
        else:
            print("Not recieving real data")
    except:
        print("Cannot parse data")
#        collection.remove({})
