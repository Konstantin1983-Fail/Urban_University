import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
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


# Создаем кнопки для Reply-клавиатуры
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
keyboard = ReplyKeyboardMarkup(resize_keyboard=True).row(button_calculate, button_info)

# Создаем Inline-кнопки и Inline-клавиатуру
button_calories = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
inline_keyboard = InlineKeyboardMarkup().add(button_calories).add(button_formulas)


# Обработчик команды /start, который выводит Reply-клавиатуру
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Выберите действие:", reply_markup=keyboard)


# Обработчик кнопки "Рассчитать" для показа Inline-клавиатуры
@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_keyboard)


# Обработчик Inline-кнопки "Формулы расчёта"
@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer(
        "Формула Миффлина-Сан Жеора:\n"
        "Для мужчин: 10 * вес + 6.25 * рост - 5 * возраст + 5\n"
        "Для женщин: 10 * вес + 6.25 * рост - 5 * возраст - 161"
    )
    await call.answer()


# Обработчик Inline-кнопки "Рассчитать норму калорий", который запускает цепочку вопросов
@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()
    await call.answer()


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
