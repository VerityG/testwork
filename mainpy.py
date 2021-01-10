from selenium import webdriver
from bs4 import BeautifulSoup
from random import randint
import requests
import json
import codecs


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


url = 'https://www.yelp.com/search?find_desc=Transmission+Repair&find_loc=San+Francisco%2C+CA&ns=1'
r = requests.get(url, headers=headers[randint(0, 2)])
print(r.content)
# if r.ok:
#     url = urls(r)
#     data_info = []
#     for i in url:
#         r = requests.get(i, headers=headers[randint(0, 2)])
#         soup = BeautifulSoup(r.content, 'html.parser')
#         data = json.loads(soup.find('script', attrs={'type': 'application/ld+json'}).string)
#         try:
#             data_info.append({'name': data['name'],'type': data['@type'], 'description': data['description'],
#                               'brand': data['brand'], 'price': data['offers']['price'], 'currency': data['offers']['priceCurrency'],
#                               'url': data['offers']['url'], 'category': data['offers']['category']})
#         except KeyError:
#             continue
#     h = codecs.open('data_pb.json', 'w', 'utf-8')
#     h.write(json.dumps(data_info, indent=2, ensure_ascii=False))
#     h.close()

