import logging
import unittest
from runner import Runner

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s | %(levelname)s | %(message)s'
)


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner('Бегун', -5)  # Попробуй создать Runner с отрицательной скоростью
        except ValueError as e:
            logging.warning("Неверная скорость для Runner", exc_info=True)
        else:
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            runner = Runner(123, 10)  # Попробуй создать Runner с числом вместо строки
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
        else:
            logging.info('"test_run" выполнен успешно')


if __name__ == '__main__':
    unittest.main()
