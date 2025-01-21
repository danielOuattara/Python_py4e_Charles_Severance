import urllib.error
import urllib.request
from bs4 import BeautifulSoup

try:
    url = input("Enter URL:\n")

    # Use 'with' to manage the context of urlopen
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, "html.parser")

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
