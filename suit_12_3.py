# Тема "Систематизация и пропуск тестов".
#Задача "Заморозка кейсов":

import unittest
import tests_12_3 #, tests_12_2

tournaments = unittest.TestSuite()

tournaments.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
tournaments.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tournaments)