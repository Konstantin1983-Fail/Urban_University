# import requests
#
# # Токен, который вы получили от @BotFather в Telegram
# TELEGRAM_TOKEN ="6426318047:AAFeHpB3kQlzCa3OK_1Kna47GCD46tzLuUs"
#
# # URL для метода API Telegram getMe
# url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/getMe'
#
# # Отправка GET-запроса на URL
# response = requests.get(url)
#
# # Проверка статуса ответа
# if response.status_code == 200:
#     # Если статус ответа 200, то токен рабочий
#     print('Токен рабочий')
# else:
#     # Если статус ответа не 200, то токен не рабочий
#     print('Токен не рабочий')


import os
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Получаем API ключ из переменных окружения
api_key = os.getenv("API_TOKEN")

# Указываем URL, к которому будем обращаться
url = "https://api.telegram.org/bot{}/getMe".format(api_key)

# Выполняем запрос и проверяем статус ответа
response = requests.get(url)
if response.status_code == 200:
    print("API ключ работает! Статус:", response.status_code)
else:
    print("Проблема с API ключом. Статус:", response.status_code)

