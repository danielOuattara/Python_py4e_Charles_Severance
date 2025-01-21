import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def url_retriever(
    url="http://py4e-data.dr-chuck.net/known_by_Mhirren.html",
    relative_position=18
):
    """
    This function read the HTML of a given web page, and 
    returns an url from a specific `relative_position`. 

    By default, `relative_position=18`, 

    `:param url: (str)`, a url indicating the web page where to search, 

    `:param relative_position: (int)`, indicates the relative_position of the 
    url to retrieve in the page, 

    `:return new_url : (str)` the retrieved url
    """

    link = None
    with urlopen(url, context=ctx) as res:
        html = res.read()
        soup = BeautifulSoup(html, "html.parser")
        tags = soup("a")
        count = 0
        for tag in tags:
            count += 1
            if count == relative_position:
                link = tag.get('href', None)
    return link


def links_follower(repeat=7):
    """
    `:param repeat: (int)`, the number of time to loop. Default is 7 times

    `:return:` This function returns the firstName in URL after repeat-times 
    loops calling `url_retriever()` function
    """

    link = None
    for counter in range(1, repeat):
        if counter == 1:
            link = url_retriever()
        link = url_retriever(link)

    firstname = re.findall(r"known_by_([A-Za-z]+)\.", link)
    return firstname[0]


print(links_follower())
