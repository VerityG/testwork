import codecs
from random import randint
import requests
import json
from bs4 import BeautifulSoup


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



url = 'https://www.pullandbear.com/by/%D0%B4%D0%BB%D1%8F-%D0%BC%D1%83%D0%B6%D1%87%D0%B8%D0%BD/%D0%BD%D0%BE%D0%B2%D0%B8%D0%BD%D0%BA%D0%B8/%D1%85%D1%83%D0%B4%D0%B8-%D1%81-%D0%BF%D1%80%D0%B8%D0%BD%D1%82%D0%BE%D0%BC-%C2%AB%D1%80%D1%8D%D0%BF%D0%B5%D1%80-%D1%82%D1%83%D0%BF%D0%B0%D0%BA%C2%BB-c1030017537p502559114.html?cS=800'
r = requests.get(url, headers=headers[randint(0, 2)])
if r.ok:
    soup = BeautifulSoup(r.content, 'html.parser')
    # main = soup.find('script', attrs={'type': 'application/ld+json'})
    data = json.loads(soup.find('script', attrs={'type': 'application/ld+json'}).string)
    print(data)