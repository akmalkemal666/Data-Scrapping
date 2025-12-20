from selenium import webdriver
from bs4 import BeautifulSoup
import fungsi
import requests
import os

def main_scraper(url):
    # headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
    driver = webdriver.Chrome()
    # driver.set_page_load_timeout(5000)
    full_url = f"{url}"
    driver.get(full_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    hasil = soup.find_all("div", class_='latest--news mt2 clearfix')
    
    for i in range(len(hasil)):
        articles = hasil[i].find_all("div", {'class':'article__list clearfix'})
        for article in articles:
            Judul = article.find("a", {'class':'article__link'})
            if Judul:
                print("Judul : " + Judul.text.strip())
                print("=====================================")

    fungsi.create_directory('hasil')
    file_path = os.path.join('hasil', 'kompasparser.txt')
    fungsi.write_to_file(file_path, html)
    # print(html)

main_scraper("https://tekno.kompas.com/gadget")