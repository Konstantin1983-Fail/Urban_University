import math

class Figure:
    """
    Базовый класс для всех геометрических фигур.
    """
    sides_count = 0  # Количество сторон фигуры

    def __init__(self, color, *sides):
        """
        Инициализация фигуры.

        :param color: Цвет фигуры в формате RGB (три целых числа от 0 до 255)
        :param sides: Стороны фигуры (целые положительные числа)
        """
        self.__color = [0, 0, 0]  # Инициализация цвета по умолчанию
        self.set_color(*color)  # Установка цвета через метод set_color
        self.filled = True  # Флаг, указывающий, закрашена ли фигура
        self.__sides = self.__initialize_sides(sides)  # Инициализация сторон фигуры через метод __initialize_sides

    def __initialize_sides(self, sides):
        """
        Инициализация сторон фигуры.

        Если количество переданных сторон не совпадает с sides_count,
        то стороны инициализируются единичными значениями.

        :param sides: Стороны фигуры
        :return: Список сторон фигуры
        """
        if len(sides) != self.sides_count:
            return [1] * self.sides_count
        return list(sides)

    def __is_valid_color(self, r, g, b):
        """
        Проверка корректности цвета.

        :param r: Значение красного канала
        :param g: Значение зеленого канала
        :param b: Значение синего канала
        :return: True, если цвет корректен, иначе False
        """
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        """
        Установка цвета фигуры.

        :param r: Значение красного канала
        :param g: Значение зеленого канала
        :param b: Значение синего канала
        """
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        """
        Получение цвета фигуры.

        :return: Цвет фигуры в формате RGB
        """
        return self.__color

    def __is_valid_sides(self, *new_sides):
        """
        Проверка корректности сторон фигуры.

        :param new_sides: Новые стороны фигуры
        :return: True, если стороны корректны, иначе False
        """
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        """
        Получение сторон фигуры.

        :return: Список сторон фигуры
        """
        return self.__sides

    def __len__(self):
        """
        Периметр фигуры.

        :return: Сумма всех сторон фигуры
        """
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        """
        Установка новых сторон фигуры.

        :param new_sides: Новые стороны фигуры
        """
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    """
    Класс для круга.
    """
    sides_count = 1  # У круга одна сторона - длина окружности

    def __init__(self, color, *sides):
        """
        Инициализация круга.

        :param color: Цвет круга в формате RGB
        :param sides: Длина окружности круга
        """
        super().__init__(color, *sides)
        self.__radius = self.__calculate_radius()  # Расчет радиуса круга

    def __calculate_radius(self):
        """
        Расчет радиуса круга.

        :return: Радиус круга
        """
        return self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        """
        Площадь круга.

        :return: Площадь круга
        """
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    """
    Класс для треугольника.
    """
    sides_count = 3  # У треугольника три стороны

    def get_square(self):
        """
        Площадь треугольника.

        Используется формула Герона для расчета площади.

        :return: Площадь треугольника
        """
        a, b, c = self.get_sides()
        p = (a + b + c) / 2  # Полупериметр
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    """
    Класс для куба.
    """
    sides_count = 12  # У куба 12 сторон (ребер)

    def __init__(self, color, *sides):
        """
        Инициализация куба.

        :param color: Цвет куба в формате RGB
        :param sides: Длина ребра куба
        """
        super().__init__(color, *sides)
        # Если передана хотя бы одна сторона, инициализируем все стороны этой величиной
        if sides:
            self._Figure__sides = [sides[0]] * 12
        else:
            self._Figure__sides = [1] * 12  # Если не переданы стороны, инициализируем единичными значениями

    def get_volume(self):
        """
        Объем куба.

        :return: Объем куба
        """
        return self._Figure__sides[0] ** 3


# Пример использования классов
circle1 = Circle((200, 200, 100), 10)  # Создание круга с цветом (200, 200, 100) и длиной окружности 10
cube1 = Cube((222, 35, 130), 6)  # Создание куба с цветом (222, 35, 130) и длиной ребра 6

# Проверка на изменение цветов
circle1.set_color(55, 66, 77)  # Изменение цвета круга
print(circle1.get_color())  # Вывод нового цвета круга
cube1.set_color(300, 70, 15)  # Попытка изменения цвета куба на некорректный
print(cube1.get_color())  # Вывод цвета куба (не изменится)

# Проверка на изменение сторон
cube1.set_sides(5, 3, 12, 4, 5)  # Попытка изменения сторон куба на некорректные
print(cube1.get_sides())  # Вывод сторон куба (не изменится)
circle1.set_sides(15)  # Изменение длины окружности круга
print(circle1.get_sides())  # Вывод новой длины окружности круга

# Проверка периметра (длины окружности) круга
print(len(circle1))  # Вывод длины окружности круга

# Проверка объема куба
print(cube1.get_volume())  # Вывод объема куба
