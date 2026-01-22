from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/detik-populer")
def detik_populer():
    html_doc = requests.get("https://www.detik.com/jatim/berita/indeks")
    soup = BeautifulSoup(html_doc.text, 'html.parser')

    populer_area = soup.find(attrs={'class': 'grid-row list-content'})
    items = populer_area.find_all(attrs={'class': 'list-content__item'})

    data = []

    for i, item in enumerate(items, start=1):
        img = item.find('img')['src']
        title = item.find('img').get('title', '')
        link = item.find('a')['href']
        date = item.find('div', {'class': 'media__date'}).find('span')['title']

        color = "merah" if is_prime(i) else "hijau"

        data.append({
            "no": i,
            "img": img,
            "title": title,
            "link": link,
            "date": date,
            "color": color
        })

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)