from bs4 import BeautifulSoup
with open("page.html") as e:
    html = BeautifulSoup(e.read(), "html.parser")

recswithads = html.find(class_="recsListing")
rectitles = recswithads.select('a[href^="/book/show"]')
rawrecdescriptions = recswithads.find(class_="bookTitle")

titles = []
prefixlink = "goodreads.com"
for i in rectitles:
    link = str(i.get("href"))
    link = prefixlink + link
    image = i.find("img")
    name = image.get("alt")
    titles.append([name , link])
print(titles)