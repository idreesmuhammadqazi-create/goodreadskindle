from bs4 import BeautifulSoup
import html
import re


data = []
exists = set()

with open("recs.html") as e:
    page = BeautifulSoup(e.read(), "html.parser")

recswithads = page.find(class_="recsListing")
for s in page.find_all("script"):
    if "bookCover" not in (s.string or '') :
        pass
    else :
        with open("tmp.txt", "w" ) as t:
            t.write(s.string)
        with open("tmp.txt", "r") as t:
            text = t.read()
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
            

            print(description)
            
            
            
            if bookid in exists :
                pass
            else:
                row = [title , author , description , link]
                exists.add(bookid)
                data.append(row)
            
            
with open("data.txt" , "w") as d:
    d.write(str(data))