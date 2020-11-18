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


url = 'https://www.mebelshara.ru/contacts'
r = requests.get(url, headers=headers[randint(0, 2)])
if r.ok:
    data_info = []
    soup = BeautifulSoup(r.content, 'html.parser')
    main_div = soup.find('div', class_='city-list js-city-list')
    div_list = main_div.findAll('div', attrs={'data-shop-name': True})
    for div in div_list:
        address = div.get('data-shop-address')
        location1 = div.get('data-shop-latitude')
        location2 = div.get('data-shop-longitude')
        name = div.get('data-shop-name')
        phone = div.get('data-shop-phone')
        work = div.get('data-shop-mode1') + div.get('data-shop-mode2')
        data_info.append({'address': address, 'location': f'{location1}, {location2}', 'name': name, 'phones': phone,
                          'working_hours': work})
    h = codecs.open('data_mebel.json', 'w', 'utf-8')
    h.write(json.dumps(data_info, indent=2, ensure_ascii=False))
    h.close()
