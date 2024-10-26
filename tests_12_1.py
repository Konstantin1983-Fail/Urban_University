# test_runner.py

import unittest
from runner import Runner  # Предполагаем, что класс Runner находится в файле runner.py

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner("Тестовый бегун")  # Создаем объект класса Runner
        for _ in range(10):  # Вызываем метод walk 10 раз
            runner.walk()
        self.assertEqual(runner.distance, 50)  # Проверяем, что distance равен 50

    def test_run(self):
        runner = Runner("Тестовый бегун")  # Создаем объект класса Runner
        for _ in range(10):  # Вызываем метод run 10 раз
            runner.run()
        self.assertEqual(runner.distance, 100)  # Проверяем, что distance равен 100

    def test_challenge(self):
        runner1 = Runner("Бегун 1")  # Создаем первого бегуна
        runner2 = Runner("Бегун 2")  # Создаем второго бегуна
        for _ in range(10):
            runner1.run()  # Вызываем метод run у первого бегуна
            runner2.walk()  # Вызываем метод walk у второго бегуна
        self.assertNotEqual(runner1.distance, runner2.distance)  # Проверяем, что дистанции разные

if __name__ == "__main__":
    unittest.main()
