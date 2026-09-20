## FOR THE FUTURE SO I CAN GET BOOK REVIEWS TOO


import re
import json
import sys
import requests

def getdescription(link):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Sec-Ch-Ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1"
    }
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
