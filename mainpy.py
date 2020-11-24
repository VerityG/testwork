from selenium import webdriver
from bs4 import BeautifulSoup
import json
import codecs


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')



data_info = []
driver = webdriver.Chrome(options=options)
driver.get('https://www.reserved.com/ru/ru/yw284-99x/yw284-99x-t01-sweter-m-re')
page_source = driver.page_source
try:
    color = driver.find_element_by_css_selector('button img[title]').get_attribute('title')
except:
    color = ''
driver.quit()
soup = BeautifulSoup(page_source, 'lxml')
id = soup.find('span', attrs={'data-selen':"sku"}).text
name = soup.find('h1', attrs={'class': 'product-name'}).text
price = soup.find('meta', {'property': 'product:price:amount'}).get('content')
currency = soup.find('meta', {'property': 'product:price:currency'}).get('content')
img = soup.find('div', {'class': 'swipe gallery-swipe'}).find('img').get('src')
data_info.append(
    {'id': id, 'Name': name, 'Price': price, 'currency': currency, 'Image': img, 'ProductLink': '', 'Brand': 'Reserved', 'Color': color})
print(data_info)
