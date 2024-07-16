import requests
import json

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

api_key = None  # Replace with your actual API key

if not api_key:
    api_key = '42'
    service_url = 'http://py4e-data.dr-chuck.net/json'
else:
    service_url = 'https://maps.googleapis.com/maps/api/geocode/json'


def get_geocode_data(address, api_key):
    params = {
        'address': address,
        'key': api_key
    }
    try:
        res = requests.get(service_url, params=params)
        res.raise_for_status()
        print('Retrieved', res.url)
        return res.json()
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving data: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None


def main():
    while True:
        address = input('Enter location: ')
        if not address:
            break

        data = get_geocode_data(address, api_key)

        if not data or 'status' not in data or data['status'] != 'OK':
            print("==== Failure To Retrieve ====")
            print(data)
            continue

        print(json.dumps(data, indent=4))

        try:
            lat = data['results'][0]['geometry']['location']['lat']
            lng = data['results'][0]['geometry']['location']['lng']
            location = data['results'][0]['formatted_address']
            print(f'lat: {lat}, lng: {lng}')
            print(f'Location: {location}')
        except (IndexError, KeyError) as e:
            print(f"Error parsing data: {e}")


if __name__ == "__main__":
    main()
