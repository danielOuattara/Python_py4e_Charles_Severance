from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1634175.html"
with urlopen(url, context=ctx) as res:
    html = res.read()
    soup = BeautifulSoup(html, "html.parser")

# Retrieve all the span tags
tags = soup("span")
count = 0
total = 0
for tag in tags:
    count += 1
    total += int(tag.contents[0])

print("count = ", count)
print("total = ", total)
