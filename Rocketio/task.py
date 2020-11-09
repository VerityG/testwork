import codecs
from random import randint
import requests
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}


session = requests.session()

url = 'https://www.tui.ru/'
r = session.get(url, headers=headers)
print(r.headers.items())
if r.ok:
    data_info = []
    soup = BeautifulSoup(r.text, 'html.parser')
    main_div = soup.find('div', attrs={'id': 'app'})
    div_list = main_div.findAll('a', class_='office-card-small ')
    a = 1