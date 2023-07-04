import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('NEW_WEATHER_API_KEY')
url = 'http://api.weatherapi.com/v1/current.json'
headers = {
    'key': API_KEY,
    'q': 'auto:ip',
    'lang': 'ru'
}

location = input('Location? (auto-detected if this field is empty): ')
if location != '':
    headers['q'] = location

response = requests.get(url=url, params=headers).json()

city_name = response["location"]["name"]
print(f'Location: {city_name}')
current_temperature = response['current']['temp_c']
print(f"Current temperature: {current_temperature}")
current_date = response["location"]["localtime"]
print(f"Current date: {current_date}")
