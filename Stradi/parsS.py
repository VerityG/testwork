import codecs
from random import randint
import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import lxml


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
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)
    driver.get(x)
    time.sleep(15)
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    page_source = driver.find_elements_by_css_selector('a#hrefRedirectProduct')
    for i in page_source:
        url_list.append(i.get_attribute('href'))
    driver.quit()
    return url_list


url = 'https://www.stradivarius.com/by/%D0%BD%D0%BE%D0%B2%D0%BE%D0%B9-%D0%BA%D0%BE%D0%BB%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D0%B8/%D0%BE%D0%B4%D0%B5%D0%B6%D0%B4%D0%B0/%D0%BA%D1%83%D0%BF%D0%B8%D1%82%D1%8C-%D0%BF%D0%BE-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D1%83/%D1%80%D1%83%D0%B1%D0%B0%D1%88%D0%BA%D0%B8/%D1%81%D0%BC%D0%BE%D1%82%D1%80%D0%B5%D1%82%D1%8C-%D0%B2%D1%81%D0%B5-c1020047030.html'
r = requests.get(url, headers=headers[randint(0, 2)])
if r.ok:
    urls = urls(url)
    data_info = []
    for i in urls:
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        driver = webdriver.Chrome(options=options)
        driver.get(i)
        driver.maximize_window()
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
    h = codecs.open('data_rbsh.json', 'w', 'utf-8')
    h.write(json.dumps(data_info, indent=2, ensure_ascii=False))
    h.close()
