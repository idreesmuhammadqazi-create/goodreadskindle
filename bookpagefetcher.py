import requests
import os
from dotenv import load_dotenv
load_dotenv()
from bs4 import BeautifulSoup

token = os.getenv("APIKEY")
def fetchpage(link):
    params = {
        "timeout": 60000,
        "token": token,
    }

    payload = {
        "url": link,
        "formats": ["html"],
    }

    response = requests.post("https://production-sfo.browserless.io/smart-scrape", params=params, json=payload, timeout=90,
    )

    response.raise_for_status()
    data = response.json()
    
    page = BeautifulSoup(data.get("content"), 'html.parser')
    page = page.prettify()
    with open("page.html", "w") as p:
        p.write(page)
