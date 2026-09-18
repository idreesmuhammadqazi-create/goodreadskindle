from bs4 import BeautifulSoup
data = []

with open("page.html") as e:
    html = BeautifulSoup(e.read(), "html.parser")

recswithads = html.find(class_="recsListing")
for s in html.find_all("script"):
    if "bookCover" not in (s.string or '') :
        pass
    else :
        with open("tmp.txt", "w" ) as t:
            t.write(s.string)
        
        with open("tmp.txt", "r") as t:
            text = t.read()
            rawtitle = text.split("<h2>")[1].split(r"<\/h2>")[0]
            link = rawtitle.split(r'href=\"')[1].split(r'">')[0]
            title = rawtitle.split(r'false\">')[1].split(r'<\/a>')[0]
            author = text.split(r"origin=recs_landing\">")[1].split(r'<\/a>')[0]
            row = [title , author , link]
            data.append(row)
            
            

print(data)
