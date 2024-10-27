class Product:
    def __init__(self, name, weight, category):
        # Инициализация атрибутов класса
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        # Возвращает строку с информацией о продукте
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self):
        # Инкапсулированное имя файла
        self.__file_name = 'products.txt'

    def get_products(self):
        # Чтение данных из файла
        try:
            with open(self.__file_name, 'r') as file:
                # Считываем всё содержимое файла
                content = file.read().strip()
            return content
        except FileNotFoundError:
            # Если файл не найден, возвращаем пустую строку
            return ""

    def add(self, *products):
        # Добавление продуктов в файл
        existing_products = self.get_products()
        with open(self.__file_name, 'a') as file:
            for product in products:
                product_str = str(product)
                # Проверка на наличие продукта в файле
                if product_str not in existing_products:
                    # Если продукта нет, добавляем его
                    file.write(product_str + '\n')
                else:
                    # Если продукт уже существует, выводим сообщение
                    print(f"Продукт {product_str} уже есть в магазине")


# Создаем экземпляр магазина
s1 = Shop()

# Создаем экземпляры продуктов
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

# Выводим продукт на экран
print(p2)  # Ожидается: Spaghetti, 3.4, Groceries

# Добавляем продукты в магазин
s1.add(p1, p2, p3)

# Получаем список всех продуктов
print(s1.get_products())
