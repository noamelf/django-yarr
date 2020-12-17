
from bs4 import BeautifulSoup

import requests as req
from feedgen.feed import FeedGenerator

resp = req.get('https://www.haaretz.co.il/misc/writers/WRITER-1.681400')

soup = BeautifulSoup(resp.text, 'lxml')

for elem in soup.find_all('article'):
    link = elem.find_all('a')[0].attrs['href']
    print(link)
    title = elem.find_all('a')[0].text
    if not title:
        title = elem.find_all('a')[1].text
    print(title)
    if elem.find('time'):
        date=elem.find('time').attrs['datetime']
        print(date)

