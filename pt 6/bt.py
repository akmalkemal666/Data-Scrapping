from bs4 import BeautifulSoup
from os import system
import fungsi
import requests 
import os

def main_scrapper(url, directory, file):
    fungsi.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")
    # articles = soup.find_all("h3", {"class":["article__title article__title--medium"]})
    articles2 = soup.find_all(True,{"class":["clearfix"]})
    

    system("clear")

    # for article in articles:
    #     print("URL: ", article.a.get("href"))
    #     print("Title: ", articles.a.text, "\n")

    articles2 = articles2[:3]

    
    for article2 in articles2:
        print("URL: ", article2.a.get("href"))
        print("Title: ", article2.a.text, "\n")
        file_path = os.path.join(directory, file)
        fungsi.write_to_file(file_path, "URL: " + article2.a.get("href")) #mengambil isi tag
        fungsi.write_to_file(file_path, "Title: " + article2.a.text + "\n")


main_scrapper("https://tekno.kompas.com/read/2025/10/29/18580047/menggenggam-realme-15t-5g-hp-tipis-baterai-besar-yang-ringan-di-tangan", "hasill", "art.txt")

# fungsi.read_data("hasill/art.txt")