# urllib + ssl + json
import ssl
import urllib.error
import urllib.parse
import urllib.request
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

api_key = False

if api_key is False:
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/json?'
else:
    service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'


def data_extractor():
    while True:
        address = input('Enter location: ')
        if len(address) < 1:
            break

        params = dict(address=address, key=api_key)
        url = service_url + urllib.parse.urlencode(params)

        print('Retrieving', url)
        url_open = urllib.request.urlopen(url, context=ctx)
        data = url_open.read().decode()
        print('Retrieved', len(data), 'characters')

        try:
            data_dict = json.loads(data)
        except:
            data_dict = None

        if not data_dict \
                or 'status' not in data_dict \
                or data_dict['status'] != 'OK':
            print('==== Failure To Retrieve ====')
            print(data)
            continue

        print('Place id ',  data_dict['results'][0]['place_id'])


data_extractor()
