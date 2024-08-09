class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        # Извлекаем название дома из аргументов
        name = args[0] if args else "Unnamed"
        # Добавляем название дома в историю
        cls.houses_history.append(name)
        # Создаем новый объект
        return super().__new__(cls)

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # Ожидаем ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # Ожидаем ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 15)
print(House.houses_history)  # Ожидаем ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

del h2
del h3

print(House.houses_history)  # Ожидаем ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
