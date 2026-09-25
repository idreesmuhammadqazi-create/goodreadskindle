from bs4 import BeautifulSoup
import html
import dotenv
import re
import os
import base64
import requests
from flask import Flask, render_template, request 
import http.cookiejar
import http
from random_header_generator import HeaderGenerator

exists = set()
data = []
app = Flask(__name__)
dotenv.load_dotenv()

def booksearch(query):
    url = "https://www.goodreads.com/search"
    params = {
        "q" : query
    }

    headers = HeaderGenerator()()
    cookies = http.cookiejar.MozillaCookieJar("cookies.txt")
    cookies.load(ignore_discard=True,ignore_expires=True)
    response = requests.get(url , params=params, headers=headers )
    page = BeautifulSoup(response.text, "html.parser")
    page = page.prettify()
    longlist = re.search(r'<ul aria-label="Book search results" class="Books" data-testid="book-list-item" role="list">(.*?)</ul>' , page , re.DOTALL)
    longlist = longlist.group(0)
    labels = re.findall(r' <a aria-label="[^"]+" class="BookCard__stretchedLink" href="[^"]+" rel="noopener noreferrer" tabindex="-1">' , longlist)
    results = []
    index = 0
    for e in labels:
        title = re.search(r'<a aria-label="(.*?)"' , e)
        title = title.group(1)
        link = re.search(r'href="(.*?)"' , e)
        link = link.group(1)
        link = "https://goodreads.com" + link
        results.append([title , link])
    return results



def dataparser():
    cookiesenv = os.getenv("COOKIES")
    cookiesenv = base64.b64decode(cookiesenv).decode("UTF-8")
    with open("cookies.txt" , "w") as c:
        c.write(cookiesenv)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:155.0) Gecko/20100101 Firefox/155.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Priority': 'u=0, i',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1'
    }
    cookies = http.cookiejar.MozillaCookieJar("cookies.txt")
    cookies.load(ignore_discard=True,ignore_expires=True)
    response = requests.get("https://goodreads.com/recommendations" , headers=headers , cookies=cookies)
    page = BeautifulSoup(response.text, "html.parser")

    for s in page.find_all("script"):
        if "bookCover" not in (s.string or '') :
            pass
        else :
            text = s.string
            rawtitle = text.split("<h2>")[1].split(r"<\/h2>")[0]
            link = rawtitle.split(r'href=\"')[1].split(r'\">')[0]
            link = link.split("?")[0]
            bookid = link.split(r"book/show/")[1].split(r"-")[0]
            title = rawtitle.split(r'false\">')[1].split(r'<\/a>')[0]
            title = html.unescape(title)
            author = text.split(r"origin=recs_landing\">")[1].split(r'<\/a>')[0]
            description = re.search(r'style=\\"display:none\\">(.*?)<\\/span>' , text , re.DOTALL)
            if description != None :
                description = description.group(1)
                description = description.replace(r"\n", "\n").replace(r"\'", "'").replace(r"\"", '"')
                description =html.unescape(description).strip()

            if bookid in exists :
                pass
            else:
                if description != None:
                    row = [title , author , description , link]
                    exists.add(bookid)
                    data.append(row)
    return(data)



@app.route("/")
def home():
    data = dataparser()
    return render_template("index.html" , data=data)

@app.route("/search" ,methods=["POST"])
def search():
    query = request.form["query"]
    results = booksearch(query)
    return render_template("search.html" , results=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)