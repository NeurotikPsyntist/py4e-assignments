import urllib.request, urllib.parse, urllib.error
import json

api_key = False

if api_key is False:
    api_key = 42
    servurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    servurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    loc = input('Enter Location: ')
    if len(loc) < 1: break
    
    locs = dict()
    locs['address'] = loc
    if api_key is not False: locs['key'] = api_key
    url = servurl + urllib.parse.urlencode(locs)

    print('Requesting URL:',url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    
    try:
        info = json.loads(data)
    except:
        info = None

    if not info or 'status' not in info or info['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    #print(json.dumps(info, indent=2))
    place_id = info['results'][0]['place_id']
    print('Place Id:',place_id)

