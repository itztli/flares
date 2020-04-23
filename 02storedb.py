#!/usr/bin/env python3
import mysql.connector
from mysql.connector import errorcode
import json
import glob
import xml.etree.ElementTree as ET
import datetime

PATH='/home/vdelaluz/public_html/static/'

#with open("db.json", "w") as write_file:
#    json.dump(config, write_file)


for filename in glob.glob(PATH+"*.xml"):
    print(filename)
    tree = ET.parse(filename)
    root = tree.getroot()
    datetime = datetime.datetime.strptime(root[0].text,'%Y-%m-%dT%H:%M:%SZ')
    flux = float(root[1].text)
    satellite = root[2].text
    print(datetime)

        
#    
#
#
#with open('db.json') as json_file:
#    config = json.load(json_file)
#
#try:
#    cnx = mysql.connector.connect(**config)
#    cursor = cnx.cursor()
#    query = ("SELECT * FROM user")
#    cursor.execute(query)
#
#    for (firstname, lastname, age) in cursor:
#        print(f"{firstname}\t{lastname}\t{age}")
#    
#except mysql.connector.Error as err:
#  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#    print("Something is wrong with your user name or password")
#  elif err.errno == errorcode.ER_BAD_DB_ERROR:
#    print("Database does not exist")
#  else:
#    print(err)
#else:
#    cnx.close()
#
