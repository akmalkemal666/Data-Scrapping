import requests
from bs4 import BeautifulSoup

html_doc = requests.get("https://www.detik.com/jatim/berita/indeks")

soup = BeautifulSoup(html_doc.text, 'html.parser')

populer_area = soup.find(attrs={'class':'grid-row list-content'})

titles = populer_area.findAll(attrs={'class':'media__title'})
images = populer_area.findAll(attrs={'class':'media__image'})
texts = populer_area.findAll(attrs={'class':'media__text'})
images = populer_area.findAll(attrs={'class':'list-content__item'})

for image in images:
    print(image.find('a').find('img'))
    print(image.find('div',{'class':'media__date'}).find('span')['title'])