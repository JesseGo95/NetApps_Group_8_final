ECE 4564
FInal Project Group 8
Find My Raspberry Pi
Yang Fei, Jesse Gora, Travis Swann, Wilber Chan

Final Files-
	gps_test.py: On the tracer pi; handles gathering GPS data from gps module, processing that data, and sending it through the XBee 
		Uses-serial, json,time, and datetime libraries
	database.py: On the server pi; handles receiving gps data from XBee, and uploads all data into MongoDB database
		Uses-pymongo, MongoClient, serial, and json libraries
	webserver.py: On server pi; accesses MongoDB and plots coordinates into Google maps API, and produces html on server
		Uses- Flask and Response (from flask library), os, pymongo, gmplot (Google maps api), time, MongoClient (from pymongo library), and BeautifulSoup (from bs4 library)
		
**The Webserver is best ran when database.py is finished running (manually with Ctrl+c)
**gps_test.py is set to run whenever the tracer pi boots up.

We had troubles getting the gps module to work, mainly because it took too long to get a fix or to keep that fix.
This is just the nature of the GPS module that we have no control over. 