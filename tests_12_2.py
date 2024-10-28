import unittest
from competition import Runner, Tournament  # Замените на реальное имя модуля


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Атрибут для хранения всех результатов
        cls.all_results = {}

    def setUp(self):
        # Создаем три объекта Runner
        self.runner1 = Runner(name="Усэйн", speed=10)
        self.runner2 = Runner(name="Андрей", speed=9)
        self.runner3 = Runner(name="Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        # Выводим все результаты
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_race_usain_and_nick(self):
        # Создаем турнир на 90 единиц дистанции
        tournament = Tournament(distance=90, participants=[self.runner1, self.runner3])
        result = tournament.start()

        # Сохраняем результат и проверяем его
        self.__class__.all_results[1] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    def test_race_andrew_and_nick(self):
        tournament = Tournament(distance=90, participants=[self.runner2, self.runner3])
        result = tournament.start()

        self.__class__.all_results[2] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    def test_race_usain_andrew_and_nick(self):
        tournament = Tournament(distance=90, participants=[self.runner1, self.runner2, self.runner3])
        result = tournament.start()

        self.__class__.all_results[3] = result
        self.assertTrue(result[max(result.keys())] == "Ник")


if __name__ == "__main__":
    unittest.main()
