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
    href = []
    soup = BeautifulSoup(x.content, 'html.parser')
    main = soup.findAll('noscript')[1]
    link = main.findAll('a')
    for div in link:
        href.append(div.get('href'))
    return href


url = 'https://www.pullandbear.com/by/%D0%B4%D0%BB%D1%8F-%D0%BC%D1%83%D0%B6%D1%87%D0%B8%D0%BD/%D0%BD%D0%BE%D0%B2%D0%B8%D0%BD%D0%BA%D0%B8-c1030017537.html'
r = requests.get(url, headers=headers[randint(0, 2)])
if r.ok:
    url = urls(r)
    data_info = []
    for i in url:
        r = requests.get(i, headers=headers[randint(0, 2)])
        soup = BeautifulSoup(r.content, 'html.parser')
        data = json.loads(soup.find('script', attrs={'type': 'application/ld+json'}).string)
        try:
            data_info.append({'name': data['name'],'type': data['@type'], 'description': data['description'],
                              'brand': data['brand'], 'price': data['offers']['price'], 'currency': data['offers']['priceCurrency'],
                              'url': data['offers']['url'], 'category': data['offers']['category']})
        except KeyError:
            continue
    h = codecs.open('data_pb.json', 'w', 'utf-8')
    h.write(json.dumps(data_info, indent=2, ensure_ascii=False))
    h.close()




