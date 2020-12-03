from bs4 import BeautifulSoup as bs
import requests
import json

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36', 'origin': 'https://unusualwhales.com', 'referer': 'https://unusualwhales.com/'}

s = requests.session()

## enter login info below, or make your own py and reference your login info

login_payload = {
		'email': "<EMAIL>",
		'password': "<PASSWORD>",
		}

login_req = s.post('https://phx.unusualwhales.com/api/users/login', headers=HEADERS, data=login_payload)

print(login_req.status_code)

cookies = login_req.cookies

soup = bs(s.get('https://unusualwhales.com/alerts').text, 'html.parser')

print(soup)


