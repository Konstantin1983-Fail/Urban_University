# Глобальная переменная для подсчета вызовов функций
calls = 0

# Функция для подсчета вызовов
def count_calls():
    global calls
    calls += 1

# Функция для получения информации о строке
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

# Функция для проверки наличия строки в списке
def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [item.lower() for item in list_to_search]
    return string in list_to_search

# Примеры вызова функций
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

# Вывод значения переменной calls
print(calls)