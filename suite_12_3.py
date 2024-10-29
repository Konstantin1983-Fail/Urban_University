import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создание TestSuite
suite = unittest.TestSuite()
# Используйте loadTestsFromTestCase вместо makeSuite
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

# Создание TextTestRunner
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
