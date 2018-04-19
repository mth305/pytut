from urllib import request
import json
import matplotlib.pyplot as plt
import numpy as np

api_key = "Nt7EflYycDRoM6CMVd23DQtDfNjKIgWJ8Y4Xs6sF"
url = "https://api.nasa.gov/planetary/apod?api_key=" + api_key

url = "https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={}".format(api_key)

req = request.Request(url)
res = request.urlopen(req)

d = json.loads(res.read())

asteroids = d["near_earth_objects"]

diameters = []

for a in asteroids:
    dia = a["estimated_diameter"]["kilometers"]["estimated_diameter_max"]
    diameters.append(dia)

hist, bins = np.histogram(diameters)

plt.plot(diameters)
plt.show()

plt.plot(hist)
plt.show()
