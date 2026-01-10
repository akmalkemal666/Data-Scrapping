from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_berita():
    url = "https://www.detik.com/jatim/berita/indeks"
    html_doc = requests.get(url)
    soup = BeautifulSoup(html_doc.text, "html.parser")

    populer_area = soup.find(attrs={'class': 'grid-row list-content'})

    titles = populer_area.findAll(attrs={'class': 'media__title'})
    images = populer_area.findAll(attrs={'class': 'media__image'})

    data = []

    for title, image in zip(titles, images):
        judul = title.text.strip()
        img_tag = image.find('img')
        img_url = img_tag['src'] if img_tag else ""

        data.append({
            'judul': judul,
            'gambar': img_url
        })

    return data


@app.route("/")
def index():
    berita = scrape_berita()
    return render_template("index.html", berita=berita)


if __name__ == "__main__":
    app.run(debug=True)
