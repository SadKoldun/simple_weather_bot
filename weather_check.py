import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.environ.get('NEW_WEATHER_API_KEY')
url = 'http://api.weatherapi.com/v1/current.json'
headers = {
    'key': API_KEY,
    'q': 'auto:ip',
    'lang': 'ru'
}


def get_weather(location='.'):
    return_dict = {}
    if location != '.':
        headers['q'] = location

    response = requests.get(url=url, params=headers).json()
    return_dict['city_name'] = response['location']['name']
    return_dict['current_temperature'] = response['current']['temp_c']
    return_dict['temperature_feels'] = response['current']['feelslike_c']
    return_dict['weather_condition'] = response['current']['condition']['text']
    return_dict['current_date'] = response['location']['localtime']
    return_dict['wind_speed'] = response['current']['wind_kph']
    return_dict['pressure'] = response['current']['pressure_mb']
    return_dict['uv_index'] = response['current']['uv']
    print(f"----- {return_dict['current_date']} -----")
    print(f"Location: {return_dict['city_name']}")
    print(return_dict['weather_condition'])
    print(f"Current temperature: {return_dict['current_temperature']}, feels like {return_dict['temperature_feels']}")
    print(f"Wind speed: {return_dict['wind_speed']}")

    return return_dict


get_weather()
