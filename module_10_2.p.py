from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()  # Инициализация родительского класса Thread
        self.name = name  # Имя рыцаря
        self.power = power  # Сила рыцаря
        self.enemies = 100  # Количество врагов, с которыми сражаются рыцари
        self.days = 0  # Счетчик дней сражения

    def run(self):
        print(f"{self.name}, на нас напали!")  # Сообщение о начале битвы
        while self.enemies > 0:  # Пока есть враги
            sleep(1)  # Задержка на 1 секунду (1 день сражения)
            self.days += 1  # Увеличиваем счетчик дней
            self.enemies -= self.power  # Уменьшаем количество врагов на силу рыцаря
            if self.enemies < 0:  # Если врагов меньше нуля, устанавливаем их в 0
                self.enemies = 0
            # Выводим сообщение о ходе сражения
            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")  # Сообщение о победе


# Создаем два потока для рыцарей
first_knight = Knight('Sir Lancelot', 10)  # Первый рыцарь
second_knight = Knight('Sir Galahad', 20)  # Второй рыцарь

# Запускаем потоки
first_knight.start()
second_knight.start()

# Ждем завершения обоих потоков
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражений
print("Все битвы закончились!")
