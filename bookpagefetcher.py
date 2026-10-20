## FOR THE FUTURE SO I CAN GET BOOK REVIEWS TOO


import re
import json
import sys
import requests
from bs4 import BeautifulSoup
from random_header_generator import HeaderGenerator


def getdescription(link):
    headers = HeaderGenerator()()
    page = requests.get(link, headers=headers)
    page = page.text
    rawjsonblob = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', page, re.DOTALL)
    jsonwithouttags = rawjsonblob.group(1)
    cleanjson = json.loads(jsonwithouttags)
    cleanjson = cleanjson["props"]["pageProps"]["apolloState"] ### HUGE SHOUTOUT TO havanagrawal FOR THIS (i got this from his scrapers scripts)

    for key,entry in cleanjson.items():
        if key.startswith("Book"):
            description = entry["description"]
            break
    return re.sub(r'<[^>]+>' , "", description).strip()

def getotherstuff(link):
    headers = HeaderGenerator()()
    page = requests.get(link, headers=headers)
    page = page.text
    rawjsonblob = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', page, re.DOTALL)
    jsonwithouttags = rawjsonblob.group(1)
    cleanjson = json.loads(jsonwithouttags)
    cleanjson = cleanjson["props"]["pageProps"]["apolloState"] ### HUGE SHOUTOUT TO havanagrawal FOR THIS (i got this from his scrapers scripts)
    for key,entry in cleanjson.items():
        if key.startswith("Work"):
            rating = entry["stats"]["averageRating"]
            break
    return rating


print(getotherstuff("https://www.goodreads.com/book/show/169485073-the-strength-of-the-few"))