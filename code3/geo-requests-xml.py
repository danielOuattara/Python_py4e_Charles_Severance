import requests
import xml.etree.ElementTree as ET

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/xml?'
else:
    service_url = 'https://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    payload = dict()
    payload['address'] = address
    payload['key'] = api_key

    res = requests.get(service_url, params=payload)
    print('Retrieving', res.url)
    data = res.text
    print('Retrieved', len(data), 'characters')
    print(data)

    tree = ET.fromstring(data)
    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    print(location)
