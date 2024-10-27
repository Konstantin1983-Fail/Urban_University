# Класс Horse, описывающий лошадь
class Horse:
    def __init__(self):
        self.x_distance = 0  # Пройденный путь по горизонтали
        self.sound = 'Frrr'  # Звук, который издает лошадь

    # Метод для увеличения пройденного пути по горизонтали
    def run(self, dx):
        self.x_distance += dx


# Класс Eagle, описывающий орла
class Eagle:
    def __init__(self):
        self.y_distance = 0  # Высота полета
        self.sound = 'I train, eat, sleep, and repeat'  # Звук, который издает орел

    # Метод для увеличения высоты полета
    def fly(self, dy):
        self.y_distance += dy


# Класс Pegasus, наследующий от Horse и Eagle
class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)  # Инициализация атрибутов класса Horse
        Eagle.__init__(self)  # Инициализация атрибутов класса Eagle

    # Метод для перемещения по горизонтали и вертикали
    def move(self, dx, dy):
        self.run(dx)  # Используем метод run() из класса Horse
        self.fly(dy)  # Используем метод fly() из класса Eagle

    # Метод для получения текущей позиции пегаса
    def get_pos(self):
        return self.x_distance, self.y_distance  # Возвращаем кортеж с пройденным путем и высотой

    # Метод для воспроизведения звука пегаса
    def voice(self):
        print(self.sound)  # Печатаем звук, унаследованный от Eagle


# Пример использования класса Pegasus
p1 = Pegasus()  # Создаем объект класса Pegasus

# Получаем текущую позицию (начальная точка)
print(p1.get_pos())  # Ожидаемый результат: (0, 0)

# Перемещаем пегаса и проверяем новую позицию
p1.move(10, 15)  # Переместить на 10 по горизонтали и на 15 по вертикали
print(p1.get_pos())  # Ожидаемый результат: (10, 15)

# Еще одно перемещение пегаса
p1.move(-5, 20)  # Переместить на -5 по горизонтали и на 20 по вертикали
print(p1.get_pos())  # Ожидаемый результат: (5, 35)

# Воспроизводим звук, который издает пегас
p1.voice()  # Ожидаемый результат: I train, eat, sleep, and repeat
