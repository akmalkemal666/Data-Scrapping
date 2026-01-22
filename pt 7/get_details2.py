"""
Scraper detail artikel untuk Kompas Tekno (kategori Gadget).

Alur ringkas:
- Ambil halaman listing, tulis URL dan Judul artikel ke berkas output.
- Kunjungi setiap URL artikel untuk mengambil isi (paragraf) dari halaman detail.
- Simpan isi artikel ke `hasil/detail.doc` dengan pemisah antar artikel.
"""

from bs4 import BeautifulSoup
import requests
import fungsi
import os
import platform

def get_details(url):
    """Mengambil isi artikel dari halaman detail dan menyimpannya ke file.

    Args:
        url (str): URL halaman artikel yang akan diambil kontennya.

    Side effects:
        Menambahkan teks paragraf artikel ke `hasil/detail.doc` dan menulis
        garis pemisah di akhir setiap artikel.
    """
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")

    # Elemen konten utama artikel (per 2024: div.read__content)
    divEntry = soup.find("div", {'class': 'read__content'})
    # Ambil seluruh paragraf di dalam konten utama
    paragraf = divEntry.find_all("p")
    
    # Tulis judul bagian untuk setiap artikel yang disimpan
    fungsi.write_to_file("hasil/detail.doc", "Paragraf:\n")
    for p in paragraf:
        # Simpan teks tiap paragraf ke file detail
        fungsi.write_to_file("hasil/detail.doc", p.text)
    # Garis pemisah antar artikel
    fungsi.write_to_file("hasil/detail.doc", "-"*100)

def main_scraper(url, directory, filename, detailname):
    """Mengambil daftar artikel dari halaman listing dan isi masing-masing artikel.

    Args:
        url (str): URL halaman listing artikel (kategori Gadget).
        directory (str): Nama folder keluaran (mis. "hasil").
        filename (str): Nama file untuk daftar URL/Judul (mis. "articlestitles.txt").
        detailname (str): Nama file untuk isi artikel (mis. "detail.doc").
    """
    fungsi.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")
    # Rangkaian selector untuk mencapai daftar kotak artikel pada halaman listing
    articles = soup.find("div", {"class":["row mt3 col-offset-fluid clearfix"]})
    articles2 = articles.find("div", {"class":["col-bs10-7"]})
    articles3 = articles2.find("div", {"class":["row article__wrap__grid--flex col-offset-fluid mt2"]})
    articles4 = articles3.find_all("div", {"class":["article__box"]})
    
    for article in articles4:
       # Siapkan path berkas output untuk daftar dan detail
       file_path = os.path.join(directory, filename)
       detail_path = os.path.join(directory, detailname)
       # Simpan URL dan Judul artikel ke daftar
       fungsi.write_to_file(file_path, "URL: " + article.h3.a.get("href"))
       fungsi.write_to_file(file_path, "Title: " + article.h3.text)
       fungsi.write_to_file(file_path, "Detail artikel disimpan di: " + detail_path + "\n")
       # Ambil isi artikel dari halaman detail
       get_details(article.h3.a.get("href"))

# clear terminal
if platform.system() == "Windows":
    # Windows
    os.system("cls")
else:
    # Linux/Mac
    os.system("clear")

# remove old file if exist
# Pastikan file keluaran lama dihapus agar hasil yang baru bersih
fungsi.remove_file("hasil/articlestitles.txt")
fungsi.remove_file("hasil/detail.doc")

# call main function
# Mulai proses scraping dari halaman listing kategori Gadget
main_scraper("https://tekno.kompas.com/gadget", "hasil", "articlestitles.txt", "detail.doc")