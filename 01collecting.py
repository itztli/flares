import json
import requests
import datetime
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys

arguments = sys.argv

response = requests.get("https://services.swpc.noaa.gov/json/goes/primary/xrays-6-hour.json")
data = response.json()
N = len(data)

time_vector = []
flux_vector = []

for item in data:
    #2020-03-12T18:47:00Z
    if item['energy'] == '0.1-0.8nm':
        mytime = datetime.datetime.strptime(item['time_tag'],'%Y-%m-%dT%H:%M:%SZ')
        flux = float(item['flux'])
        time_vector.append(mytime)
        flux_vector.append(flux)
        print(item['time_tag'],flux)


fig, ax = plt.subplots()
ax.plot(time_vector, flux_vector)

ax.set(xlabel='time (s)', ylabel='Flux (W m-2)',
       title='X-Ray Flux 1-Day')
ax.grid()
plt.ylim(1e-9,1e-2)
plt.yscale("log")

fig.savefig(arguments[1]+"/x-ray-flux.png")
plt.show()

#information = data[0]

#print(information['time_tag'])

#xray_flux = json.loads(response.text)
#print(xray_flux["time_tag"])
