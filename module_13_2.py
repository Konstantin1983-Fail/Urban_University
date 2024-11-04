from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import Message
import asyncio

# Загружаем переменные из .env
load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: Message):
    print("Привет! Я бот, помогающий твоему здоровью.")
    await message.reply("Привет! Я бот, помогающий твоему здоровью.")  # Отправляем сообщение пользователю


@dp.message_handler()
async def all_messages(message: Message):
    print("Введите команду /start, чтобы начать общение.")
    await message.reply("Введите команду /start, чтобы начать общение.")  # Отправляем сообщение пользователю


if __name__ == '__main__':
    print("Бот запущен и готов к работе!")
    executor.start_polling(dp, skip_updates=True)
