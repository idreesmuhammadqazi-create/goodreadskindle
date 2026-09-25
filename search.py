import requests
from bs4 import BeautifulSoup
import http
import re


query = input("enter query : ")
url = "https://www.goodreads.com/search"
params = {
    "q" : query
}

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "close",
    "Dnt": "0",
    "Pragma": "no-cache",
    "Referer": "https://www.facebook.com",
    "Upgrade-Insecure-Requests": "0",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36",
    "Sec-Ch-Ua": "\"Chromium\";v=\"118\", \"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"118\"",
    "Sec-Ch-Ua-Platform": "Android",
    "Sec-Ch-Ua-Mobile": "?1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "cache-control": "no-store"
}
cookies = http.cookiejar.MozillaCookieJar("cookies.txt")
cookies.load(ignore_discard=True,ignore_expires=True)
response = requests.get(url , params=params, headers=headers , cookies=cookies)
page = BeautifulSoup(response.text, "html.parser")
page = page.prettify()
longlist = re.search(r'<ul aria-label="Book search results" class="Books" data-testid="book-list-item" role="list">(.*?)</ul>' , page , re.DOTALL)
longlist = longlist.group(1)
with open("search.html" , "w") as s:
    s.write(longlist)
