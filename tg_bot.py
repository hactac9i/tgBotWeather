import requests
import datetime
from config import tg_bot_token, weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token = tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start'])
async def start_command(message: types.Message):
    await message.reply('Введите название города (eng/rus) ')

@dp.message_handler()
async  def get_weater(message: types.Message):
    try:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weather_token}&units=metric'
        )
        data = r.json()
        #pprint(data)

        city = data['name']
        weather_street = data['weather'][0]['main']
        cur_weather = data['main']['temp']
        feel_weather = data['main']['feels_like']
        humidity = data['main']['humidity']
        speed_wind = data['wind']['speed']
        sunrise_time = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_time = datetime.datetime.fromtimestamp(data['sys']['sunset'])

        await message.reply(f'Текущая погода в городе {city}  \n{weather_street}\nТемпература: {cur_weather} °С  \nТемпература по ощущениям: {feel_weather}°С   \nВлажность: {humidity} %  \nВремя рассвета: {sunrise_time} \nВремя заката: {sunset_time}')

    except:
        await message.reply('Неверный ввод')


if __name__ == '__main__':
    executor.start_polling(dp)