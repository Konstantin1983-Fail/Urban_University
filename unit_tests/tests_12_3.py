import unittest

class RunnerTest(unittest.TestCase):

    def test_challenge(self):
        # Ваш код теста
        self.assertTrue(True)  # Пример проверки

    def test_run(self):
        # Ваш код теста
        self.assertTrue(True)  # Пример проверки

    def test_walk(self):
        # Ваш код теста
        self.assertTrue(True)  # Пример проверки

class TournamentTest(unittest.TestCase):

    @unittest.skip("Тесты в этом кейсе заморожены")
    def test_first_tournament(self):
        # Ваш код теста
        pass

    @unittest.skip("Тесты в этом кейсе заморожены")
    def test_second_tournament(self):
        # Ваш код теста
        pass

    @unittest.skip("Тесты в этом кейсе заморожены")
    def test_third_tournament(self):
        # Ваш код теста
        pass
