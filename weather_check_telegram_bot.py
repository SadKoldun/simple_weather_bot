import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from weather_check import get_weather


load_dotenv()
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=os.environ.get("BOT_API_KEY"))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.reply("Кидай название города и я кину погоду.\nДавай.\nБыстренько.")


@dp.message_handler()
async def return_weather(message: types.message):
    location = message.text
    try:
        weather_data = get_weather(location)
        await message.reply(f"---------- {weather_data['current_date']} ----------\n\n"
                            f"Найден город: {weather_data['city_name']}\n"
                            f"{weather_data['weather_condition']}\n"
                            f"Температура {weather_data['current_temperature']} °C\n"
                            f"Ощущается как {weather_data['temperature_feels']} °C\n"
                            f"Скорость ветра: {weather_data['wind_speed']} км/ч\n"
                            f"Давление: {weather_data['pressure']}\n"
                            f"Индекс ультрафиолетового излучения: {weather_data['uv_index']}\n"
                            )
    except:
        await message.reply("Город не найден...")


executor.start_polling(dp)
