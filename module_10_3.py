import threading
import random
from time import sleep

class Bank:
    def __init__(self):
        self.balance = 0  # Изначальный баланс
        self.lock = threading.Lock()  # Создаем объект Lock

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # Генерация случайной суммы для пополнения
            with self.lock:  # Блокируем поток
                self.balance += amount  # Увеличиваем баланс
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
                # Проверка на разблокировку
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()  # Разблокируем lock
            sleep(0.001)  # Имитируем скорость выполнения пополнения

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # Генерация случайной суммы для снятия
            print(f"Запрос на {amount}")  # Сообщаем о запросе на снятие
            with self.lock:  # Блокируем поток
                if amount <= self.balance:  # Проверяем, достаточно ли средств
                    self.balance -= amount  # Уменьшаем баланс
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")  # Если средств недостаточно
                    self.lock.acquire()  # Блокируем поток

bk = Bank()

# Создаем потоки для методов deposit и take
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()  # Запускаем поток пополнения
th2.start()  # Запускаем поток снятия
th1.join()  # Ожидаем завершения потока пополнения
th2.join()  # Ожидаем завершения потока снятия

print(f'Итоговый баланс: {bk.balance}')  # Выводим итоговый баланс
