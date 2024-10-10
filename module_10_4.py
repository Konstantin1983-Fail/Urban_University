import threading
import time
import random
from queue import Queue

# Класс столов
class Table:
    def __init__(self, number):
        self.number = number  # Номер стола
        self.guest = None  # Гость, сидящий за столом (изначально пусто)

# Класс гостей, наследуется от потока
class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name  # Имя гостя

    # Метод, который запускает поток (имитация времени ожидания гостя)
    def run(self):
        wait_time = random.randint(3, 10)  # Ожидание от 3 до 10 секунд
        time.sleep(wait_time)

# Класс кафе, управляющий столами и гостями
class Cafe:
    def __init__(self, *tables):
        self.tables = list(tables)  # Список столов в кафе
        self.queue = Queue()  # Очередь для гостей, если столы заняты

    # Метод для прибытия гостей
    def guest_arrival(self, *guests):
        for guest in guests:
            table_found = False
            for table in self.tables:
                if table.guest is None:  # Если стол свободен
                    table.guest = guest  # Гость занимает стол
                    guest.start()  # Запуск потока гостя
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    table_found = True
                    break
            if not table_found:
                self.queue.put(guest)  # Добавление гостя в очередь
                print(f"{guest.name} в очереди")

    # Метод для обсуждения гостей и обработки обслуживания
    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():  # Если поток завершен
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None  # Освобождаем стол
                    if not self.queue.empty():  # Если очередь не пуста
                        new_guest = self.queue.get()  # Берем гостя из очереди
                        table.guest = new_guest  # Садим за стол
                        new_guest.start()  # Запускаем поток
                        print(f"{new_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
            time.sleep(1)

# Пример выполнения программы:
if __name__ == "__main__":
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание объектов гостей
    guests = [Guest(name) for name in guests_names]
    # Создание объекта кафе с пятью столами
    cafe = Cafe(*tables)
    # Прибытие гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()
