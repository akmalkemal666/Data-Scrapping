from selenium import webdriver

url = "https://id.indeed.com/jobs?q=part+time&l=Surabaya&ts=1764209535473&from=searchOnDesktopSerp&rq=1&rsIdx=1&newcount=8&fromage=last&vjk=9d05be9c1b8adfa2"
params = {
    'q': 'part+time',
    'l': 'Surabaya',
    'vjk': '9d05be9c1b8adfa2'
}

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
driver = webdriver.Chrome()
full_url = f"{url}&q={params['q']}&l={params['l']}"
driver.get(full_url)
html = driver.page_source

print(html)