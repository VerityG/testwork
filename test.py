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


url = 'https://www.reserved.com/ru/ru/new-in/men'
r = requests.get(url, headers=headers[randint(0, 2)])
if r.ok:
    print(r)
    urls = urls(r)
    data_info = []
    for i in urls:
        r = requests.get(i, headers=headers[randint(0, 2)])
        h = codecs.open('text.html', 'w', 'utf-8')
        h.write(r.text)
        h.close()
        a = 1
        if r.ok:
            soup = BeautifulSoup(r.content, 'html.parser')
            h = soup.find('meta', attrs={'property': 'og:description'})
            header = h.get('content')
            p = soup.find('meta', attrs={'property': 'product:original_price:amount'})
            price = p.get('content')
            i = soup.find('meta', attrs={'property': 'og:image'})
            img = i.get('content')
            data_info.append({'header': header, 'price': price, 'img': img, })
    h = codecs.open('data.json', 'w', 'utf-8')
    h.write(json.dumps(data_info, indent=2, ensure_ascii=False))
    h.close()
