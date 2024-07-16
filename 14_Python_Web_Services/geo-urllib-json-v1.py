import ssl
import urllib.error
import urllib.parse
import urllib.request
import json

"""
If you have a Google Places API key, enter it here
api_key = 'AIzaSy___IDByT70'
https://developers.google.com/maps/documentation/geocoding/intro

"""

api_key = False

if api_key is False:
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/json?'
else:
    service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Choose a location: ')
    if len(address) < 1:
        break

    params = dict()
    params['address'] = address
    params['key'] = api_key
    url = service_url + urllib.parse.urlencode(params)

    print('Retrieving', url)
    url_open = urllib.request.urlopen(url, context=ctx)
    data = url_open.read().decode()
    print('Retrieved ', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=2, sort_keys=True))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
