import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import requests

headers = {
    'User-Agent': 'Mozilla/5.0'
}

web_scrap = requests.get(
    'https://books.toscrape.com/',
    headers=headers
).text

soup = BeautifulSoup(web_scrap, 'lxml')

data = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

name = []
rating = []
price = []
stock = []
image = []

for i in data:
    name.append((i.find('h3').text.strip()))
    star =((i.find('p',class_ ='star-rating')))
    rating.append(star['class'][1])
    p = ((i.find('div',class_ = 'product_price').text.strip()))
    price.append(p[2:7])
    stock.append((i.find('p', class_ = 'instock availability').text.strip()))
    img_div = i.find_all('div', class_='image_container')
    img_tag = img_div[0].find_all('img')[0]
    src = image.append(img_tag['src'])
    
d = pd.DataFrame({
    'name': name,
    'ratig': rating,
    'price':price,
    'stock':stock,
    'image':image
})

print(d)

d.to_csv('book_data.csv',index = False)





