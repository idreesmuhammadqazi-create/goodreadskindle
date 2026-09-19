import requests
import http.cookiejar
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
print(response)
with open("recs.html", "w") as t:
    t.write(response.text)