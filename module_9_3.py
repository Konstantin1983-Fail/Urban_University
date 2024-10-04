# Даны два списка
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# 1. Генераторная сборка для вычисления разницы длин строк, если длины не равны (с использованием zip)
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

# 2. Генераторная сборка для сравнения длин строк на одинаковых позициях без использования zip
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Пример использования:
print(list(first_result))
print(list(second_result))
