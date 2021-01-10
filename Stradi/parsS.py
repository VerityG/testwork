import codecs
from random import randint
import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
import time


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
    main_div = soup.find('noscript')
    div_list = main_div.findAll('a', attrs={'href': True})
    for div in div_list:
        address = div.get('href')
        url_list.append(address)
    return url_list


url = 'https://www.stradivarius.com/by/%D0%BD%D0%BE%D0%B2%D0%BE%D0%B9-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B8/%D0%BE%D0%B4%D0%B5%D0%B6%D0%B4%D0%B0/%D0%BA%D1%83%D0%BF%D0%B8%D1%82%D1%8C-%D0%BF%D0%BE-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D1%83/%D0%BF%D0%B0%D0%BB%D1%8C%D1%82%D0%BE/%D1%81%D0%BC%D0%BE%D1%82%D1%80%D0%B5%D1%82%D1%8C-%D0%B2%D1%81%D0%B5-c1020140016.html'
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
        time.sleep(10)
        page_source = driver.page_source
        driver.quit()
        soup = BeautifulSoup(page_source, 'lxml')
        data = json.loads(soup.find('script', attrs={'type': 'application/ld+json'}).string)
        description = soup.find('div', attrs={'class': 'product-description text-transform-none block-height'}).text
        color = soup.find('div', attrs={'class': 'product-colors'}).text
        try:
            data_info.append({'name': data['name'], 'price': data['offers']['price'], 'currency': data['offers']['priceCurrency'],
                              'url': data['offers']['url'], 'image': data['image'], 'description': description,
                              'article': data['mpn'], 'color': color})
        except KeyError:
            continue
    h = codecs.open('data_plt.json', 'w', 'utf-8')
    h.write(json.dumps(data_info, indent=2, ensure_ascii=False))
    h.close()
