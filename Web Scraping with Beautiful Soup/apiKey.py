import requests

baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {'APPID': 'd840eb7583e9cd4c1fda3f7958ed57b7', 'q': 'Seattle,US'}
response = requests.get(baseUrl, params=parameters)
print(response.content)