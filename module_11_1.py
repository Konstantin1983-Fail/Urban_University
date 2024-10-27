import requests  # Импортируем библиотеку requests для работы с HTTP-запросами
import xml.etree.ElementTree as ET  # Импортируем xml.etree.ElementTree для парсинга XML-данных
import pandas as pd  # Импортируем pandas для работы с таблицами и временными рядами
import matplotlib.pyplot as plt  # Импортируем matplotlib для построения графиков
from datetime import datetime, timedelta  # Импортируем datetime и timedelta для работы с датами

# Конфигурация
URL = 'https://www.cbr.ru/scripts/XML_daily.asp'  # URL для получения XML-данных с курса валют ЦБ РФ
MONTHS_BACK = 3  # Количество месяцев назад для выборки данных

def get_current_rate():
    try:
        response = requests.get(URL)  # Выполняем GET-запрос на указанный URL
        response.raise_for_status()  # Проверяем, произошла ли ошибка при запросе
        root = ET.fromstring(response.content)  # Парсим содержимое XML-ответа
        for valute in root.findall('Valute'):  # Проходим по каждому элементу "Valute"
            if valute.find('CharCode').text == 'USD':  # Ищем элемент с кодом валюты 'USD'
                return float(valute.find('Value').text.replace(',', '.'))  # Возвращаем курс доллара, преобразуя его в число
    except (requests.RequestException, ET.ParseError) as e:  # Обрабатываем ошибки HTTP-запроса и парсинга XML
        print(f"Ошибка при получении курса: {e}")  # Выводим сообщение об ошибке
        return None  # Возвращаем None в случае ошибки

def prepare_data(current_rate):
    end_date = datetime.now()  # Определяем текущую дату
    start_date = end_date - timedelta(days=30 * MONTHS_BACK)  # Рассчитываем начальную дату, вычитая количество месяцев
    dates = pd.date_range(start=start_date, end=end_date, freq='ME')  # Создаем список последних дней месяца в заданном диапазоне

    data = {
        'Date': dates.strftime('%Y-%m-%d').tolist() + [end_date.strftime('%Y-%m-%d')],  # Форматируем даты как строки и добавляем текущую дату
        'Sales': [65.07, 78.03, 83.09, current_rate]  # Пример данных для продаж, замените на реальные данные
    }
    return pd.DataFrame(data).set_index('Date')  # Создаем DataFrame и устанавливаем индекс по дате

def plot_data(df):
    plt.style.use('ggplot')  # Устанавливаем стиль графика
    plt.figure(figsize=(10, 6))  # Настраиваем размер графика

    plt.plot(df.index, df['Sales'], marker='o', linestyle='-', color='b', label='Курс доллара')  # Строим линию курса доллара с метками
    plt.title('Курс доллара США к рублю')  # Устанавливаем заголовок графика
    plt.xlabel('Дата')  # Устанавливаем подпись для оси X
    plt.ylabel('Курс, руб.')  # Устанавливаем подпись для оси Y
    plt.xticks(rotation=45)  # Поворачиваем метки на оси X на 45 градусов
    plt.tight_layout()  # Настраиваем плотное расположение элементов графика
    plt.grid(True)  # Включаем сетку на графике

    for date, value in zip(df.index, df['Sales']):  # Добавляем текстовые метки значений на графике
        plt.text(date, value, f'{value:.2f}', ha='center', va='bottom', fontsize=9, color='black')

    plt.legend()  # Показываем легенду графика
    plt.show()  # Отображаем график

def main():
    current_rate = get_current_rate()  # Получаем текущий курс доллара
    if current_rate:  # Если курс получен успешно
        print(f"Курс доллара: {current_rate:.2f} руб.")  # Выводим курс доллара

        df = prepare_data(current_rate)  # Подготавливаем данные для анализа
        print("\n            Sales")  # Выводим заголовок таблицы
        print(df.to_string(float_format=lambda x: f'{x:,.2f}'.replace('.', ',')))  # Выводим таблицу данных, форматируя числа

        plot_data(df)  # Строим график
    else:
        print("Не удалось получить текущий курс доллара.")  # Сообщаем, если курс не был получен

if __name__ == "__main__":
    main()  # Запускаем программу
