import codecs
from random import randint
import requests
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()

headers = [{
               'User-Agent': ua.firefox,
               'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
           {
               'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
               'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
           {
               'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
               'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
           ]


session = requests.session()

url = 'https://www.tui.ru/'
r = session.get(url, headers=headers[randint(0, 2)])
print(r.cookies.items())
if r.ok:
    data_info = []
    soup = BeautifulSoup(r.text, 'html.parser')
    main_div = soup.find('div', attrs={'id': 'app'})
    div_list = main_div.findAll('a', class_='office-card-small ')
    a = 1