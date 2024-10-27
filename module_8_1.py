def add_everything_up(a, b):
    try:
        # Пытаемся выполнить сложение стандартным образом
        result = a + b
        # Если результат — float, форматируем его до 3 знаков после запятой
        if isinstance(result, float):
            return "{:.3f}".format(result)
        return result
    except TypeError:
        # Если возникает TypeError (разные типы данных), возвращаем строковое представление
        return str(a) + str(b)


# Примеры использования функции
print(add_everything_up(123.456, 'строка'))  # Выведет: 123.456строка
print(add_everything_up('яблоко', 4215))  # Выведет: яблоко4215
print(add_everything_up(123.456, 7))  # Выведет: 130.456
