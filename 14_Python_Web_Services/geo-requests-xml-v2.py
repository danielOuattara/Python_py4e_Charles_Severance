import requests
import xml.etree.ElementTree as ET

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

api_key = None  # Replace with your actual API key

if not api_key:
    api_key = '42'
    service_url = 'http://py4e-data.dr-chuck.net/xml?'
else:
    service_url = 'https://maps.googleapis.com/maps/api/geocode/xml?'


def get_geocode_data(address, api_key):
    params = {
        'address': address,
        'key': api_key
    }
    try:
        res = requests.get(service_url, params=params)
        res.raise_for_status()
        print('Retrieving', res.url)
        return res.text
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving data: {e}")
        return None


def parse_xml(data):
    try:
        tree = ET.fromstring(data)
        results = tree.findall('result')
        if not results:
            print("No results found in the XML response")
            return None, None, None
        lat = results[0].find('geometry').find('location').find('lat').text
        lng = results[0].find('geometry').find('location').find('lng').text
        location = results[0].find('formatted_address').text
        return lat, lng, location
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return None, None, None


def main():
    while True:
        address = input('Enter location: ')
        if not address:
            break

        data = get_geocode_data(address, api_key)

        if not data:
            continue

        lat, lng, location = parse_xml(data)
        if not lat or not lng or not location:
            print("==== Failure To Retrieve ====")
            print(data)
            continue

        print(f'lat: {lat}, lng: {lng}')
        print(f'Location: {location}')


if __name__ == "__main__":
    main()
