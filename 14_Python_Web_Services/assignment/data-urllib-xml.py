import ssl
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def data_extractor():
    total = 0
    service_url = input('Enter url : ')
    if not service_url:
        service_url = "http://py4e-data.dr-chuck.net/comments_1634177.xml"

    print('Retrieving', service_url)
    uh = urllib.request.urlopen(service_url, context=ctx)
    data = uh.read()

    print('Retrieved', len(data), 'characters')
    commentinfo = data.decode()
    tree = ET.fromstring(commentinfo)
    count_list = tree.findall('comments/comment')

    count = len(count_list)
    print("Count: ", count)

    for item in count_list:
        total += int(item.find('count').text)

    print("total = ", total)


data_extractor()
