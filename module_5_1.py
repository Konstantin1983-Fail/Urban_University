# Определяем класс House
class House:
    # Метод инициализации, который вызывается при создании объекта
    def __init__(self, name, number_of_floors):
        self.name = name  # Устанавливаем имя дома
        self.number_of_floors = number_of_floors  # Устанавливаем количество этажей

    # Метод для перемещения на заданный этаж
    def go_to(self, new_floor):
        # Проверяем, существует ли такой этаж
        if 1 <= new_floor <= self.number_of_floors:
            # Если этаж существует, выводим все этажи от 1 до new_floor включительно
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            # Если этаж не существует, выводим сообщение об ошибке
            print("Такого этажа не существует")


# Создаем объекты класса House
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# Вызываем метод go_to для объектов
h1.go_to(5)  # Ожидаем вывод этажей от 1 до 5
h2.go_to(10)  # Ожидаем сообщение "Такого этажа не существует"
