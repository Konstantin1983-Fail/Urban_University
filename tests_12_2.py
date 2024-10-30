import unittest
from competition import Runner, Tournament  # Замените на реальное имя модуля

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.__class__.all_results[1] = {k: str(v) for k, v in results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.__class__.all_results[2] = {k: str(v) for k, v in results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.__class__.all_results[3] = {k: str(v) for k, v in results.items()}
        self.assertTrue(results[max(results.keys())] == "Ник")

if __name__ == "__main__":
    unittest.main()
