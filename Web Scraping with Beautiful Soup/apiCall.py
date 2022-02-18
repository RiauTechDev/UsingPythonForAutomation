import requests
import json

baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameter = {'upc': '073366118238'}
response = requests.get(baseUrl, params=parameter)
print(response.url)
content = response.content
info = json.loads(content)
item = info['items']
itemInfo = item[0]
title = itemInfo['title']
brand = itemInfo['brand']
print(title)
print(brand)