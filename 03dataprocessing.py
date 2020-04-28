#!/usr/bin/env python3

# Execute a query to the database, process information and produces a simple plot.
import mysql.connector
from mysql.connector import errorcode
import json
import glob
import xml.etree.ElementTree as ET
import datetime
import subprocess
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


PATH='/home/vdelaluz/public_html/static/'

#with open("db.json", "w") as write_file:
#    json.dump(config, write_file)

with open('db.json') as json_file:
    config = json.load(json_file)

    x = []
    y = []
    
try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = ("SELECT time_tag, flux FROM FluxHighEnergy WHERE flux > 0.00000002 ORDER BY time_tag")
    #data_query = (mydate, flux, satellite)
    #print(mydate)
    cursor.execute(query)#,data_query)
    for (time_tag, flux) in cursor:
        print(f"{time_tag}\t{flux}")
        x.append(time_tag)
        y.append(flux)
        
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()


fig, ax = plt.subplots()
ax.set(xlabel='time', ylabel='flux',
       title='view2D')
#plt.axis([x_A, x_B,  y_A, y_B])
ax.grid()

ax.plot(x, y)
fig.savefig("/home/vdelaluz/public_html/static/last_flux.png")
