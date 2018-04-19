from urllib import request
import json

def get_json_response(url):
    req = request.Request(url)
    res = request.urlopen(req)
    return json.loads(res.read())

url = "https://maps.googleapis.com/maps/api/geocode/json?address=Ryparken+40"
d = get_json_response(url)
print(json.dumps(d, indent=2))

res = d["results"]
print(res)
geo = res["geometry"]
lat = geo["location"]["lat"]
lon = geo["location"]["lng"]

print(lat, lon)
