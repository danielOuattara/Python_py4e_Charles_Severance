import requests  # You need to install the requests module to use this code
import json

"""
If you have a Google Places API key, enter it here
api_key = 'AIzaSy___IDByT70'
https://developers.google.com/maps/documentation/geocoding/intro

"""

api_key = False

if api_key is False:
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/json'
else:
    service_url = 'https://maps.googleapis.com/maps/api/geocode/json'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    payload = dict()
    payload['address'] = address
    payload['key'] = api_key

    res = requests.get(service_url, params=payload)
    print('Retrieved', res.url)
    data = res.text
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)