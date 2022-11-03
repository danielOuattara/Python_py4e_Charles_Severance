import ssl
import urllib.error
import urllib.parse
import urllib.request
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def data_extractor():
    total = 0
    service_url = input('Enter url : ')
    if not service_url:
        service_url = "http://py4e-data.dr-chuck.net/comments_1634178.json"

    print('Retrieving', service_url)
    uh = urllib.request.urlopen(service_url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    try:
        data_dict = json.loads(data)
    except:
        data_dict = None

    if not data_dict:
        print('==== Failure To Retrieve ====')
        print(data)
        return

    comments = data_dict["comments"]
    count = len(comments)
    print("Count: ", count)

    for item in comments:
        total += int(item['count'])

    print("total = ", total)


data_extractor()
