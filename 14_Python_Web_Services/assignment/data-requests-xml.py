import requests
import xml.etree.ElementTree as ET


def data_extractor():
    total = 0
    service_url = input('Enter url : ')
    if not service_url:
        service_url = "http://py4e-data.dr-chuck.net/comments_1634177.xml"

    print('Retrieving', service_url)
    response = requests.get(service_url)
    data = response.text
    print('Retrieved', len(data), 'characters')

    tree = ET.fromstring(data)
    count_list = tree.findall('comments/comment')

    count = len(count_list)
    print("Count: ", count)

    for item in count_list:
        total += int(item.find('count').text)

    print("total = ", total)


data_extractor()
