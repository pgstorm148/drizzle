from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
print("enter website address")
a=input()
req = Request(a)
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

print(links)

