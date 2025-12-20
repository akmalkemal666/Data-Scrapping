from selenium import webdriver
from bs4 import BeautifulSoup
import fungsi
import requests
import os
import time

def main_scraper(url):

    driver = webdriver.Chrome()
    driver.set_page_load_timeout(5000)
    driver.get(url)

    # tunggu javascript load
    time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # selector yang benar
    hasil = soup.find_all("article", class_="latest--news mt2 clearfix")

    for item in hasil:
        Card = item.find("div", {'class':'article__list clearfix'})
        Judul = item.find("a", {'class':'article__link'})
        
        if Card and Judul:
            print("Card  : ", Card.text.strip())
            print("Judul : ", Judul.text.strip())
            print("=====================================")

    # simpan file
    fungsi.create_directory('hasil')
    file_path = os.path.join('hasil', 'kompasparser.txt')
    fungsi.write_to_file(file_path, html)

    driver.quit()


main_scraper("https://tekno.kompas.com/gadget")