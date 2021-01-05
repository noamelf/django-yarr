from datetime import datetime

from bs4 import BeautifulSoup

import requests as req
from feedgen.feed import FeedGenerator
author_link= 'https://www.haaretz.co.il/misc/writers/WRITER-1.850'
resp = req.get('https://www.haaretz.co.il/misc/writers/WRITER-1.850')

soup = BeautifulSoup(resp.text, 'lxml')

author= soup.find_all('section')[0].find_all('div')[2].text
print(author)
fg = FeedGenerator()
fg.link(href = author_link)
fg.author({'name':author})
fg.title(author)
fg.description(author)
fg.language('he')
for elem in soup.find_all('article'):
    link = elem.find_all('a')[0].attrs['href']
    print(link)
    title = elem.find_all('a')[0].text
    if not title:``
        title = elem.find_all('a')[1].text
    print(title)
    if elem.find('time'):
        date = elem.find('time').attrs['datetime']
        print(date)
    else:
        print(datetime.now())
    fe = fg.add_entry()
    fe.id(link)
    fe.title(title)
    fe.link(href=link)
    fe.pubDate(date)
    print(fe)

fg.rss_file('test-data',pretty=True)

