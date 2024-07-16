import urllib.request
import urllib.parse
import urllib.error
import json
import twurl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'


def get_twitter_data(acct):
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    try:
        connection = urllib.request.urlopen(url)
        data = connection.read().decode()
        headers = dict(connection.getheaders())
        print('Remaining', headers.get('x-rate-limit-remaining', 'Unknown'))
        return json.loads(data)
    except urllib.error.URLError as e:
        print(f"Error retrieving data: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None


def main():
    while True:
        print('')
        acct = input('Enter Twitter Account: ')
        if not acct:
            break

        data = get_twitter_data(acct)
        if not data:
            continue

        print(json.dumps(data, indent=4))

        for u in data.get('users', []):
            print(u['screen_name'])
            status = u.get('status', {}).get('text', 'No status available')
            print('  ', status[:50])


if __name__ == "__main__":
    main()
