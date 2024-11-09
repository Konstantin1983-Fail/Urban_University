from dotenv import load_dotenv  # Используем dotenv для загрузки переменных окружения
import os
from aiogram import Bot, Dispatcher, types, executor

# Загружаем переменные из файла .env
load_dotenv()

# Получаем токен бота из переменных окружения
API_TOKEN = os.getenv("API_TOKEN")

# Проверяем, что токен не пустой
if not API_TOKEN:
    raise ValueError("API_TOKEN не найден. Проверьте .env файл.")

# Создаем объекты бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Обработчик для команды /start
@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.")


# Обработчик для всех остальных сообщений
@dp.message_handler()
async def all_message(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
