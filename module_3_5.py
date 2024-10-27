def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Извлекаем первую цифру
    first = int(str_number[0])

    # Условие для окончания рекурсии
    if len(str_number) == 1:
        return first
    else:
        # Рекурсивный вызов функции для оставшихся цифр
        return first * get_multiplied_digits(int(str_number[1:]))


# Пример вызова функции и вывод результата
result = get_multiplied_digits(40203)
print(result)  # Должен вывести: 24

