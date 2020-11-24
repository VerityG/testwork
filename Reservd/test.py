import codecs
from random import randint
import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver


headers = [{
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/81.0.4044.138 Safari/537.36',
    'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.3987.132 Safari/537.36',
        'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.3987.132 Safari/537.36',
        'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
]


def urls(x):
    url_list = []
    soup = BeautifulSoup(x.content, 'html.parser')
    main_div = soup.find('section', class_=True)
    div_list = main_div.findAll('article', attrs={'data-sku': True})
    for div in div_list:
        a = div.find('a', class_=True)
        address = a.get('href')
        url_list.append(address)
    return url_list


url = 'https://www.reserved.com/ru/ru/man/clothes/shirts'
r = requests.get(url, headers=headers[randint(0, 2)])
if r.ok:
    urls = urls(r)
    data_info = []
    for i in urls:
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        driver = webdriver.Chrome(options=options)
        driver.get(i)
        page_source = driver.page_source
        try:
            color = driver.find_element_by_css_selector('button img[title]').get_attribute('title')
        except:
            color = ''
        driver.quit()
        soup = BeautifulSoup(page_source, 'lxml')
        id = soup.find('span', attrs={'data-selen': "sku"}).text
        name = soup.find('h1', attrs={'class': 'product-name'}).text
        price = soup.find('meta', {'property': 'product:price:amount'}).get('content')
        currency = soup.find('meta', {'property': 'product:price:currency'}).get('content')
        img = soup.find('div', {'class': 'swipe gallery-swipe'}).find('img').get('src')
        data_info.append({'id': id, 'name': name, 'price': price,'currency': currency, 'image': img, 'productlink': i,
                          'brand': 'Reserved','color': color})
    h = codecs.open('data.json', 'w', 'utf-8')
    h.write(json.dumps(data_info, indent=2, ensure_ascii=False))
    h.close()
