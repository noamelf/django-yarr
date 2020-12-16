from bs4 import BeautifulSoup
import requests as req

resp = req.get('https://www.haaretz.co.il/misc/writers/WRITER-1.681400')

soup = BeautifulSoup(resp.text, 'lxml')

print(soup.title)
print(soup.title.text)
print(soup.title.parent)