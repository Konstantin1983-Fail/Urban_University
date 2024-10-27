def personal_sum(numbers):
    result = 0  # Для хранения суммы чисел
    incorrect_data = 0  # Для подсчета некорректных данных

    # Проходим по каждому элементу коллекции numbers
    for item in numbers:
        try:
            result += item  # Пытаемся добавить элемент к сумме
        except TypeError:
            print(f"Некорректный тип данных для подсчёта суммы - {item}")
            incorrect_data += 1  # Увеличиваем счетчик некорректных данных

    return result, incorrect_data


def calculate_average(numbers):
    try:
        # Используем функцию personal_sum для подсчета суммы
        total_sum, incorrect_data = personal_sum(numbers)

        # Проверяем, не является ли numbers пустым
        if len(numbers) - incorrect_data == 0:
            raise ZeroDivisionError  # Если все данные некорректные, вызовем это исключение

        # Вычисляем среднее арифметическое
        return total_sum / (len(numbers) - incorrect_data)

    except ZeroDivisionError:
        # Если деление на ноль, возвращаем 0
        return 0
    except TypeError:
        # Если передан некорректный тип данных
        print('В numbers записан некорректный тип данных')
        return None


# Примеры использования
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Числа и строки
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Только числа
