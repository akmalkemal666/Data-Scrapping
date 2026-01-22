from bs4 import BeautifulSoup
import requests
import fungsi
import os
import platform

def get_details(url):
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")
    divEntry = soup.find("div", {'class': 'read__content'})
    paragraf = divEntry.find_all("p")
    
    fungsi.write_to_file("hasil/detail.doc", "Paragraf:\n")
    for p in paragraf:
        fungsi.write_to_file("hasil/detail.doc", p.text)
    fungsi.write_to_file("hasil/detail.doc", "-"*100)

def main_scraper(url, directory, filename, detailname):
    fungsi.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")
    articles = soup.find("div", {"class":["row mt3 col-offset-fluid clearfix"]})
    articles2 = articles.find("div", {"class":["col-bs10-7"]})
    articles3 = articles2.find("div", {"class":["row article__wrap__grid--flex col-offset-fluid mt2"]})
    articles4 = articles3.find_all("div", {"class":["article__box"]})
    
    for article in articles4:
       file_path = os.path.join(directory, filename)
       detail_path = os.path.join(directory, detailname)
       fungsi.write_to_file(file_path, "URL: " + article.h3.a.get("href"))
       fungsi.write_to_file(file_path, "Title: " + article.h3.text)
       fungsi.write_to_file(file_path, "Detail artikel disimpan di: " + detail_path + "\n")
       get_details(article.h3.a.get("href"))

# clear terminal
if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear") # Linux/Mac

# remove old file if exist
fungsi.remove_file("hasil/articlestitles.txt")
fungsi.remove_file("hasil/detail.doc")

# call main function
main_scraper("https://tekno.kompas.com/gadget", "hasil", "articlestitles.txt", "detail.doc")