def calculate_structure_sum(data):
    # Инициализируем переменную для хранения общей суммы
    total_sum = 0

    # Вложенная функция для рекурсивного обхода структуры данных
    def recursive_sum(item):
        nonlocal total_sum  # Используем nonlocal, чтобы модифицировать total_sum внутри вложенной функции
        # Если элемент является числом, добавляем его к общей сумме
        if isinstance(item, (int, float)):
            total_sum += item
        # Если элемент является строкой, добавляем её длину к общей сумме
        elif isinstance(item, str):
            total_sum += len(item)
        # Если элемент является списком, кортежем или множеством, рекурсивно обходим его элементы
        elif isinstance(item, list) or isinstance(item, tuple) or isinstance(item, set):
            for elem in item:
                recursive_sum(elem)
        # Если элемент является словарём, рекурсивно обходим его ключи и значения
        elif isinstance(item, dict):
            for key, value in item.items():
                recursive_sum(key)  # Обработка ключа
                recursive_sum(value)  # Обработка значения

    # Начинаем рекурсивный обход с переданного элемента данных
    recursive_sum(data)
    # Возвращаем вычисленную сумму
    return total_sum

# Пример использования функции
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# Вызываем функцию и выводим результат
result = calculate_structure_sum(data_structure)
print(result)  # Ожидаемый вывод: 99


