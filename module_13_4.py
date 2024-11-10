import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # Импортируем хранилище для работы с состояниями
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

# Создаем бота и инициализируем хранилище состояний
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()  # Хранилище для хранения данных FSM в оперативной памяти
# (подходит для отладки и небольших ботов)
dp = Dispatcher(bot, storage=storage)  # Создаем диспетчер и передаем в него хранилище
dp.middleware.setup(LoggingMiddleware())  # Устанавливаем middleware для логирования


# Создаем класс состояний пользователя
class UserState(StatesGroup):
    age = State()  # Состояние для ввода возраста
    growth = State()  # Состояние для ввода роста
    weight = State()  # Состояние для ввода веса


# Обработчик для команды "Calories" - запуск цепочки вопросов
@dp.message_handler(lambda message: message.text.lower() == 'calories', state="*")
async def set_age(message: types.Message):
    await message.answer("Введите свой возраст:")  # Просим ввести возраст
    await UserState.age.set()  # Устанавливаем состояние для ввода возраста


# Обработчик для состояния UserState.age - обработка возраста
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)  # Сохраняем введенный возраст в хранилище
    await message.answer("Введите свой рост:")  # Просим ввести рост
    await UserState.growth.set()  # Устанавливаем состояние для ввода роста


# Обработчик для состояния UserState.growth - обработка роста
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)  # Сохраняем введенный рост в хранилище
    await message.answer("Введите свой вес:")  # Просим ввести вес
    await UserState.weight.set()  # Устанавливаем состояние для ввода веса


# Обработчик для состояния UserState.weight - обработка веса и расчет калорий
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)  # Сохраняем введенный вес в хранилище

    # Получаем все данные, введенные пользователем
    data = await state.get_data()
    age = int(data['age'])  # Преобразуем возраст в число
    growth = int(data['growth'])  # Преобразуем рост в число
    weight = int(data['weight'])  # Преобразуем вес в число

    # Расчет нормы калорий по формуле Миффлина-Сан Жеора для мужчин
    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    # Отправляем результат пользователю
    await message.answer(f"Ваша норма калорий: {calories} ккал в день")

    # Завершаем машину состояний, очищаем данные
    await state.finish()


# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)  # Начинаем получать обновления
