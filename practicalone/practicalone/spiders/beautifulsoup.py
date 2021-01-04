import requests
from bs4 import BeautifulSoup
r = requests.get('https://quotes.toscrape.com')

soup = BeautifulSoup(r.content, 'lxml')

quotes = soup.find_all('div', class_="quote")
for x in quotes:
    print(x.find('span').text)

tags = soup.find_all("div", class_='tags')
for y in tags:
    print(y.text)