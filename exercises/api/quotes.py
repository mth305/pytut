from urllib import request
import json


url = " http://quotes.rest/qod.json"
req = request.Request(url)
res = request.urlopen(req)

d = json.loads(res.read())
print(d)
