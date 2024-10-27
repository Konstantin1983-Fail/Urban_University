def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызовы функции с разными параметрами
print_params()  # Должен вывести: 1 'строка' True
print_params(b=25)  # Должен вывести: 1 25 True
print_params(c=[1, 2, 3])  # Должен вывести: 1 'строка' [1, 2, 3]

# Список и словарь для распаковки параметров
values_list = [42, 'hello', False]
values_dict = {'a': 10, 'b': 'world', 'c': None}

# Вызов функции с распаковкой параметров
print_params(*values_list)  # Должен вывести: 42 'hello' False
print_params(**values_dict)  # Должен вывести: 10 'world' None

# Второй список для частичной распаковки параметров
values_list_2 = [54.32, 'Строка']

# Вызов функции с частичной распаковкой параметров
print_params(*values_list_2, 42)  # Должен вывести: 54.32 'Строка' 42

