import requests
from pprint import pprint
from config import weather_token
import datetime


def get_weather(city, weather_token):
    try:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric'
        )
        data = r.json()
        #pprint(data)

        city = data['name']

        cur_weather = data['main']['temp']
        feel_weather = data['main']['feels_like']
        humidity = data['main']['humidity']
        speed_wind = data['wind']['speed']
        sunrise_time = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_time = datetime.datetime.fromtimestamp(data['sys']['sunset'])

        print(f'Текущая погода в городе {city}  \nТемпература: {cur_weather} °С  \nТемпература по ощущениям: {feel_weather}°С   \nВлажность: {humidity} %  \nВремя рассвета: {sunrise_time} \nВремя заката: {sunset_time}')

    except Exception as ex:
        print(ex)
        print('Неверный ввод')

def main():
    city = input('Введите город: ')
    get_weather(city, weather_token)

if __name__ == ' __main__':
    main()
