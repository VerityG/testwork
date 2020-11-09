import requests

proxy = {'https': 'localhost:8080'}

r = requests.get('https://www.tui.ru/offices/', proxies=proxy, verify=False)


