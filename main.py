# Погода через API

import requests
from PIL import Image
import io

API_KEY = 'f0aafc86eb5c1b35632e4504ffd88dfc'
URL = 'http://api.openweathermap.org/data/2.5/weather'
CITY = 'Варшава'

params = {
    'q': CITY,
    'appid': API_KEY,
    'units': 'metric',
    'lang': 'ru'
}

response = requests.get(URL, params=params)
result = response.json()
weather = result['weather'][0]['description']
temperature = result['main']['temp']
humidity = result['main']['humidity']
wind = result['wind']['speed']

data = result['coord']
ll = f'{data['lon']},{data['lat']}'

link = f'https://static-maps.yandex.ru/1.x/?ll={ll}&spn=0.005,0.005&l=sat&pt={ll},pm2dgl'
image = requests.get(link).content
if image:
    im = Image.open(io.BytesIO(image)).convert('RGB')
    im.save('./images/mapvarshava.jpg')



print(f'Сегодня в городе {CITY}: {weather}')
print(f'Температура: {temperature:.1f}°C')
print(f'Влажность: {humidity}%')
print(f'Скорость ветра: {wind} м/с')
