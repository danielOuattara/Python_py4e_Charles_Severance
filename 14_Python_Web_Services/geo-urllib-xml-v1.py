import ssl
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

"""
If you have a Google Places API key, enter it here
api_key = 'AIzaSy___IDByT70'
https://developers.google.com/maps/documentation/geocoding/intro

"""
api_key = False

if api_key is False:
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/xml?'
else:
    service_url = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    params = dict()
    params['address'] = address
    params['key'] = api_key

    url = service_url + urllib.parse.urlencode(params)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())

    tree = ET.fromstring(data)
    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    print(location)
