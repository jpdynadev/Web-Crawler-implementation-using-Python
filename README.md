# Web-Crawler-implementation-using-Python
Web Crawler implementation using Python

###WebCrawlerPython.py

There are three methods in this script:

  1. findDomain <- finds root domain using tld library
  ```
  def findDomain(url):
    root = get_tld(url, as_object=True)
    return root.fld[0:root.fld.find('.')]
  ```
  2. valid_url <- validates url using urlparse library
  ```
  def valid_url(url):
    validated = urlparse(url)
    return bool(validated.scheme) and bool(validated.netloc)

  ```
  3. getLinks <- retrieves url content using BeautifulSoup
  ```
  def getLinks(url):
    links = {}
    domain = findDomain(url)
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
  ```
Initialize dictionary for links, find root domain using helper method, and parse html content using BeautifulSoup

```
    for link in  soup.findAll("a"):
        if(len(links) == 25):
            return links
        valid = link.attrs.get("href")
        if valid == "" or valid is None:
            continue
        if not valid_url(valid):
            continue
```
  for every link we find all the a tags, if links dictionary size is 25, return links
  if not we get the href link, and validate that it is not empty or null
  we also check that it is a valid url
```
        if domain in valid and "#" not in valid:
```

check if root domain is in the link, and that we are not calling any internal page links. 

```
            try:
                temp = urllib2.urlopen(valid).read()
                
```
Use urllib2 to retrieve html content to insert into dictionary

```
            except Exception:
                continue
            print("adding link to list: ", valid)
            links[valid] = temp

    return links

```

Once dictionary has been completed the script will write all items into Links.txt in json format:

```
with open("Links.txt", "w") as file:
        for links in urls:
            file.write("{ 'link' : '" + str(links) + "', '\n'")
            file.write(" 'url' : '" + str(urls[links]) + "' }")
```
