import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.amazon.com/Best-Sellers/zgbs')

soup = BeautifulSoup(r.content, 'lxml')

rating = soup.find_all('a', class_="a-size-small a-link-normal")
data = [x.text for x in rating]

import pandas as pd

data = hasil()
data = pd.DataFrame(data)