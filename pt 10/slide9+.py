from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://id.indeed.com/jobs?q=web+developer&l=jawa+timur&from=searchOnHP%2Cwhatautocomplete%2CwhatautocompleteSourceStandard&vjk=f918e7918fa63c19"
params = {
    'q': 'web+developer',
    'l': 'jawa+timur'
}
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
driver = webdriver.Chrome()
full_url = f"{url}q={params['q']}&l={params['l']}"
driver.get(full_url)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
data = soup.find_all("div", class_='jobsearch-InfoHeaderContainer css-jpohn6 eu4oa1w0')
for i in range(len(data)):
    Pekerjaan = data[i].find("h2", {'class':'class="jobsearch-JobInfoHeader-title css-16tttqo e1tiznh50"'})
    Perusahaan = data[i].find("span", {'class':'css-qcqa6h e1wnkr790'})
    Lokasi = data[i].find("div", {'class':'css-89aoy7 eu4oa1w0'})
    if Pekerjaan and Perusahaan and Lokasi:
        print("Pekerjaan : " + Pekerjaan.text)
        print("Perusahaan : " + Perusahaan.text)
        print("Lokasi : " + Lokasi.text)
        print("=====================================")

print(data)
driver.quit()

def get_total_page():
    with open('temp/res.html', 'w', encoding='utf-8') as file:
        file.write(html)

    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find('ul', class_='css-pygyny eu4oa1w0')
    print(pagination)

if __name__ == '__main__':
    get_total_page()