import requests
from tld import get_tld
from urlparse import urlparse, urljoin
from bs4 import BeautifulSoup
import json
import urllib2
"""
WebCrawler implementation in Python by J.P. Florez
"""

def findDomain(url):
    root = get_tld(url, as_object=True)
    return root.fld[0:root.fld.find('.')]
def valid_url(url):
    validated = urlparse(url)
    return bool(validated.scheme) and bool(validated.netloc)

def getLinks(url):
    links = {}
    domain = findDomain(url)
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    for link in  soup.findAll("a"):
        if(len(links) == 25):
            return links
        valid = link.attrs.get("href")
        if valid == "" or valid is None:
            continue
        if not valid_url(valid):
            continue
        if domain in valid and "#" not in valid:
            try:
                temp = urllib2.urlopen(valid).read()
            except Exception:
                continue
            print("adding link to list: ", valid)
            links[valid] = temp

    return links



if __name__ == "__main__":
    url = raw_input("Please enter URL to parse: ")
    while(not(valid_url(url))):
        url = raw_input("Not valid url - please enter valid url: ")

    urls = getLinks(url)

    with open("Links.txt", "w") as file:
        for links in urls:
            file.write("{ 'link' : '" + str(links) + "', '\n'")
            file.write(" 'url' : '" + str(urls[links]) + "' }")

