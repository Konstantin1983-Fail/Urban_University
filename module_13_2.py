from dotenv import load_dotenv  # Импортируем функцию для загрузки переменных окружения из файла .env
import os  # Импортируем модуль для работы с операционной системой
from aiogram import Bot, Dispatcher, types  # Импортируем необходимые классы из библиотеки aiogram
from aiogram.utils import executor  # Импортируем executor для запуска бота
from aiogram.types import Message  # Импортируем класс Message для работы с сообщениями
import asyncio  # Импортируем asyncio для работы с асинхронным кодом

# Загружаем переменные из .env
load_dotenv()

# Получаем токен API из переменных окружения
API_TOKEN = os.getenv('API_TOKEN')
bot = Bot(token=API_TOKEN)  # Создаем экземпляр бота с токеном
dp = Dispatcher(bot)  # Создаем диспетчер для обработки обновлений


@dp.message_handler(commands=['start'])  # Обработчик команды /start
async def start(message: Message):
    print("Привет! Я бот, помогающий твоему здоровью.")  # Выводим сообщение в консоль
    await message.reply("Привет! Я бот, помогающий твоему здоровью.")  # Отправляем сообщение пользователю


@dp.message_handler()  # Обработчик всех остальных сообщений
async def all_messages(message: Message):
    print("Введите команду /start, чтобы начать общение.")  # Выводим сообщение в консоль
    await message.reply("Введите команду /start, чтобы начать общение.")  # Отправляем сообщение пользователю


if __name__ == '__main__':
    print("Бот запущен и готов к работе!")  # Сообщаем о запуске бота
    executor.start_polling(dp, skip_updates=True)  # Запускаем бота и пропускаем старые обновления
