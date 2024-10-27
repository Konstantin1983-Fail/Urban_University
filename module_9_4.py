from random import choice

# Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'

# Lambda-функция для покомпонентного сравнения символов строк
result = list(map(lambda x, y: x == y, first, second))

print(result)

# Замыкание
def get_advanced_writer(file_name):
    # Функция записи всех данных в файл
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for data in data_set:
                f.write(str(data) + '\n')  # Записываем каждое значение на новой строке
    return write_everything

# Пример использования замыкания:
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Класс с методом __call__
class MysticBall:
    def __init__(self, *words):
        self.words = words

    # Метод __call__, который позволяет объекту класса быть вызываемым как функция
    def __call__(self):
        return choice(self.words)

# Пример использования метода __call__:
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
