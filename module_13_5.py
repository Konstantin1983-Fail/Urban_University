import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

# Загрузка переменных окружения из .env
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())


# Создаем класс состояний пользователя
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# Создаем кнопки для клавиатуры
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')

# Создаем клавиатуру с кнопками
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.row(button_calculate, button_info)


# Обработчик команды /start, который выводит клавиатуру
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Выберите действие:", reply_markup=keyboard)


# Обработчик кнопки "Рассчитать", который запускает цепочку вопросов
@dp.message_handler(lambda message: message.text == 'Рассчитать', state="*")
async def set_age(message: types.Message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()


# Обработчик для состояния UserState.age - запрос роста
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


# Обработчик для состояния UserState.growth - запрос веса
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


# Обработчик для состояния UserState.weight - расчет калорий
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # Формула расчета калорий
    calories = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f"Ваша норма калорий: {calories} ккал в день")
    await state.finish()


# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
