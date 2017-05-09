import sys
import pymongo
from pymongo import MongoClient
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebView
import gmplot

client = MongoClient('localhost')
db = client.test_database
collection = db.test_collection

lats = []
longs = []
for post in collection.find():
    print(post)
    lats.append(post["lat"])
    longs.append(post["long"])

gmap = gmplot.GoogleMapPlotter(lats[0], longs[0], 15)
gmap.scatter(lats, longs, "red", size=40, markers = True)
gmap.plot(lats, longs)
gmap.circle(lats[-1], longs[-1], 50, 'red')
gmap.draw("mymap.html")

app = QApplication(sys.argv)
view = QWebView()
view.load(QUrl('mymap.html'))
view.show()
app.exec_()
