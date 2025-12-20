from bs4 import BeautifulSoup
import os
import requests
import fungsi1

def main_scraper(url, directory):
    # Pastikan folder hasil ada
    fungsi1.create_directory(directory)

    # Ambil HTML
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text, "html.parser")

    # Ambil semua artikel di halaman gadget Kompas
    articles = soup.find_all("div", class_="article__list")

    # Buat file hasil scraping
    file_path = f"{directory}/hasil_kompas.txt"
    fungsi1.create_new_file(file_path)

    print(f"🔍 Ditemukan {len(articles)} artikel di halaman {url}\n")

    for i, article in enumerate(articles[:10], start=1):  # ambil 10 pertama
        # Ambil judul
        title_tag = article.find("h3", class_="article__title")
        judul = title_tag.get_text(strip=True) if title_tag else "Judul tidak ditemukan"

        # Ambil link
        link = title_tag.find("a")["href"] if title_tag and title_tag.find("a") else "Link tidak tersedia"

        # Ambil tanggal
        date_tag = article.find("div", class_="article__date")
        tanggal = date_tag.get_text(strip=True) if date_tag else "Tanggal tidak ditemukan"

        print(f"{i}. {judul}")
        print(f"   Link: {link}")
        print(f"   Tanggal: {tanggal}\n")

        # Simpan ke file
        fungsi1.write_to_file(file_path, f"{i}. {judul}\n   {tanggal}\n   {link}\n")

    print(f"\n✅ Hasil scraping disimpan di: {file_path}")

# Jalankan fungsi utama
main_scraper("https://tekno.kompas.com/gadget", "Hasil")
