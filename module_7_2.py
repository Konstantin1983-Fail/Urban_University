def custom_write(file_name, strings):
    # Открываем файл в режиме записи с кодировкой utf-8
    with open(file_name, 'w', encoding='utf-8') as file:
        strings_positions = {}  # Словарь для сохранения позиций и строк
        for i, string in enumerate(strings, start=1):
            # Получаем текущую позицию байта перед записью строки
            position = file.tell()
            # Записываем строку в файл, добавляя символ новой строки
            file.write(string + '\n')
            # Сохраняем номер строки и позицию в словарь
            strings_positions[(i, position)] = string
    return strings_positions  # Возвращаем словарь с позициями и строками

# Пример использования функции
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

# Выводим результат на экран
for elem in result.items():
    print(elem)
