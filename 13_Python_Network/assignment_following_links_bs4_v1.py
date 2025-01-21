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
    position=18
):
    """
    This function returns an url from a specific position in a web page. 
    By default, position=18, 
    :param url: (str) url indicating the web page 
    where to search, 
    :param position: (int) indicates the position of the 
    url to retrieve in the page, 
    :return new_url : (str) the retrieved url
    """

    res = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(res, "html.parser")
    tags = soup("a")
    count = 0
    for tag in tags:
        count += 1
        if count != 18:
            continue
        link = tag.get('href', None)
        return link


def links_follower(repeat=7):
    """
    :param repeat: (int) the number of time to loop. Default is 7 times
    :return: This function returns the firstName in URL after repeat-times 
    loops calling url_retriever() function
    """

    link = None
    while repeat > 0:
        if repeat == 7:
            repeat -= 1
            link = url_retriever()
        else:
            repeat -= 1
            url_retriever(link)
            link = url_retriever(link)
            # print(link)
    firstname = re.findall(r"known_by_([A-Za-z]+)\.", link)
    print(link)
    return firstname[0]


print(links_follower())
