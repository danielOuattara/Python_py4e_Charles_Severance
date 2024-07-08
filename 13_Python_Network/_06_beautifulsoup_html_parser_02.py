import urllib.error
import urllib.request
from bs4 import BeautifulSoup

try:
    url = input("Enter URL: ")
    res = urllib.request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(res, "html.parser")

    # Retrieve all the anchor tags
    tags = soup.find_all("a")
    for tag in tags:
        href = tag.get('href')
        if href:
            print(href)

except urllib.error.URLError as e:
    print(f"Error fetching URL: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
