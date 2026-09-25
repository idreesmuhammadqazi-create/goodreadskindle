import requests
from bs4 import BeautifulSoup
import http
import re
from random_header_generator import HeaderGenerator

query = "mistborn"
url = "https://www.goodreads.com/search"
params = {
    "q" : query
}

headers = HeaderGenerator()()
print(headers)
print("--------------------------")
cookies = http.cookiejar.MozillaCookieJar("cookies.txt")
cookies.load(ignore_discard=True,ignore_expires=True)
response = requests.get(url , params=params, headers=headers , cookies=cookies)
page = BeautifulSoup(response.text, "html.parser")
page = page.prettify()
longlist = re.search(r'<ul aria-label="Book search results" class="Books" data-testid="book-list-item" role="list">(.*?)</ul>' , page , re.DOTALL)
longlist = longlist.group(0)
labels = re.findall(r' <a aria-label="[^"]+" class="BookCard__stretchedLink" href="[^"]+" rel="noopener noreferrer" tabindex="-1">' , longlist)
titles = []
links = []
index = 0
for e in labels:
    title = re.search(r'<a aria-label="(.*?)"' , e)
    title = title.group(1)
    print(title)
    titles.append(title)
    link = re.search(r'href="(.*?)"' , e)
    link = link.group(1)
    link = "https://goodreads.com" + link
    print(link)
    links.append(link)
    index = index + 1
