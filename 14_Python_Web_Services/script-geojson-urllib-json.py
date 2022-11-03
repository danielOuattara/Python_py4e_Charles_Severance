"""
http://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%2C+MI

Using google map API and entering the above URL, we get the json document
below:

{
    "status": "OK",
    "results": [
        {
            "geometry": {
                "location_type": "APPROXIMATE",
                "location": {
                    "lat": 42.2808256,
                    "lng": -83.7430378
                }
            },
            "address_components": [
                {
                    "long_name": "Ann Arbor",
                    "types": [
                        "locality",
                        "political"
                    ],
                    "short_name": "Ann Arbor"
                }
            ],
            "formatted_address": "Ann Arbor, MI, USA",
            "types": [
                "locality",
                "political"
            ]
        }
    ]
}
-------------------------------------------------------------------------------
"""

import json
import urllib.error
import urllib.parse
import urllib.request

service_url = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break
    url = service_url + urllib.parse.urlencode({'address': address})
    print('Retrieving', url)
    res = urllib.request.urlopen(url)
    data = res.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        break
    else:
        lat = js["results"][0]["geometry"]["location"]["lat"]
        lng = js["results"][0]["geometry"]["location"]["lng"]
        print('lat', lat, 'lng', lng)
        location = js['results'][0]['formatted_address']
        print(location)
