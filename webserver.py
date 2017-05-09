from flask import Flask, Response
import os
import pymongo
import gmplot
import time
from pymongo import MongoClient
from bs4 import BeautifulSoup

def insertapikey(fname, apikey):
    """put the google api key in a html file"""
    def putkey(htmltxt, apikey, apistring=None):
        """put the apikey in the htmltxt and return soup"""
        if not apistring:
            apistring = "https://maps.googleapis.com/maps/api/js?key=%s&callback=initMap"
        soup = BeautifulSoup(htmltxt, 'html.parser')
        body = soup.body
        src = apistring % (apikey, )
        tscript = soup.new_tag("script", src=src, async="defer")
        body.insert(-1, tscript)
        return soup
    htmltxt = open(fname, 'r').read()
    soup = putkey(htmltxt, apikey)
    newtxt = soup.prettify()
    return newtxt

app = Flask(__name__)

def root_dir():
    return os.path.abspath(os.path.dirname(__file__))

def get_file(filename):
    try:
        return open(filename).read()
    except IOError as exc:
        return str(exc)

@app.route('/')
def map():
    client = MongoClient('localhost')
    db = client.test_database
    collection = db.test_collection

    lats = []
    longs = []
    for post in collection.find():
        #print(post)
        lats.append(post["lat"])
        longs.append(post["long"])

    gmap = gmplot.GoogleMapPlotter(lats[0], longs[0], 15)
    #gmap.scatter(lats, longs, "red", size=40, markers = True)
    gmap.plot(lats, longs)
    for i in range(len(lats)-1):
        gmap.circle(lats[i], longs[i], 30, 'blue')
        
    gmap.circle(lats[-1], longs[-1], 50, 'red')
    gmap.draw("mymap.html")
    txt = insertapikey("mymap.html", "AIzaSyCN07DloisyucyBJcPLKfGvZDgqq0L-hCw")
    txt = txt.replace('async="defer"', "async defer")
    txt = txt.replace('amp;',"")
    print(txt)
    return txt

app.run(host='172.29.78.197')
