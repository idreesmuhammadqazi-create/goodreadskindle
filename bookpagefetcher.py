## FOR THE FUTURE SO I CAN GET BOOK REVIEWS TOO


import re
import json
import sys
import requests
from bs4 import BeautifulSoup
from random_header_generator import HeaderGenerator


def makecleanjson(link):
    headers = HeaderGenerator()()
    page = requests.get(link, headers=headers)
    page = page.text
    rawjsonblob = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', page, re.DOTALL)
    jsonwithouttags = rawjsonblob.group(1)
    cleanjson = json.loads(jsonwithouttags)
    cleanjson = cleanjson["props"]["pageProps"]["apolloState"] ### HUGE SHOUTOUT TO havanagrawal FOR THIS (i got this from his scrapers scripts)
    return cleanjson

def getreviews(cleanjson):
    reviews = []
    for key,entry in cleanjson.items():
        if key.startswith("Review:"):
            reviewtext = entry["text"]
            reviewrating = entry["rating"]
            reviews.append([reviewtext , reviewrating])
    return reviews

def getrating(cleanjson):
    for key,entry in cleanjson.items():
        if key.startswith("Work"):
            rating = entry["stats"]["averageRating"]
            break
    return rating

def getdescription(cleanjson):
    for key,entry in cleanjson.items():
        if key.startswith("Book"):
            description = entry["description"]
            break
    return re.sub(r'<[^>]+>' , "", description).strip()