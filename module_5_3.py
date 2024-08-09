class House:
    def __init__(self, name, number_of_floors):
        # Инициализация объекта. name - название дома, number_of_floors - количество этажей
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        # Метод возвращает строковое представление объекта House
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        # Метод сравнивает два объекта House на равенство по количеству этажей
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False  # Если other не является объектом класса House, возвращаем False

    def __lt__(self, other):
        # Метод сравнивает два объекта House: меньше ли self, чем other по количеству этажей
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return NotImplemented  # Если other не является объектом класса House, возвращаем NotImplemented

    def __le__(self, other):
        # Метод сравнивает два объекта House: меньше или равно ли self, чем other по количеству этажей
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return NotImplemented  # Если other не является объектом класса House, возвращаем NotImplemented

    def __gt__(self, other):
        # Метод сравнивает два объекта House: больше ли self, чем other по количеству этажей
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return NotImplemented  # Если other не является объектом класса House, возвращаем NotImplemented

    def __ge__(self, other):
        # Метод сравнивает два объекта House: больше или равно ли self, чем other по количеству этажей
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return NotImplemented  # Если other не является объектом класса House, возвращаем NotImplemented

    def __ne__(self, other):
        # Метод сравнивает два объекта House на неравенство по количеству этажей
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return NotImplemented  # Если other не является объектом класса House, возвращаем NotImplemented

    def __add__(self, value):
        # Метод увеличивает количество этажей на заданное значение (value)
        if isinstance(value, int):
            self.number_of_floors += value
            return self  # Возвращаем сам объект с обновленным количеством этажей
        return NotImplemented  # Если value не является целым числом, возвращаем NotImplemented

    def __radd__(self, value):
        # Метод для поддержки операции value + self
        # Просто вызываем __add__, так как порядок операндов не имеет значения для сложения
        return self.__add__(value)

    def __iadd__(self, value):
        # Метод для поддержки операции +=
        # Просто вызываем __add__, чтобы увеличить количество этажей и сохранить изменения в том же объекте
        return self.__add__(value)

# Тестирование
h1 = House('ЖК Эльбрус', 10)  # Создаем объект House с названием "ЖК Эльбрус" и 10 этажами
h2 = House('ЖК Акация', 20)   # Создаем объект House с названием "ЖК Акация" и 20 этажами

print(h1)  # Выводим строковое представление h1
print(h2)  # Выводим строковое представление h2

print(h1 == h2)  # Проверяем равны ли объекты h1 и h2 по количеству этажей (False)

h1 = h1 + 10  # Увеличиваем количество этажей в h1 на 10
print(h1)  # Выводим строковое представление h1 после изменения (20 этажей)

print(h1 == h2)  # Проверяем равны ли объекты h1 и h2 после изменения (True)

h1 += 10  # Еще раз увеличиваем количество этажей в h1 на 10 с помощью операции +=
print(h1)  # Выводим строковое представление h1 после второго изменения (30 этажей)

h2 = 10 + h2  # Увеличиваем количество этажей в h2 на 10 с помощью операции 10 + h2
print(h2)  # Выводим строковое представление h2 после изменения (30 этажей)

# Проверяем результаты сравнений между h1 и h2
print(h1 > h2)  # Проверяем, больше ли h1 чем h2 (False)
print(h1 >= h2)  # Проверяем, больше или равно ли h1 чем h2 (True)
print(h1 < h2)  # Проверяем, меньше ли h1 чем h2 (False)
print(h1 <= h2)  # Проверяем, меньше или равно ли h1 чем h2 (True)
print(h1 != h2)  # Проверяем, не равны ли h1 и h2 (False)
