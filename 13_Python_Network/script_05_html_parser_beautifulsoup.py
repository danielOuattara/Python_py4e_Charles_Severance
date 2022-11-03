import urllib.error
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

url = input("Enter  - ")
res = urllib.request.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

# Retrieve all the anchor tags
tags = soup("a")
for tag in tags:
    print(tag.get('href', None))
