# Тема "Простые Юнит-Тесты"   (tests_12_1)
# Задача "Проверка на выносливость"

import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0


    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = False  # новый аттрибут

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner1 = Runner("I")
        for i in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner2 = Runner("You")
        for i in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner3 = Runner("He")
        runner4 = Runner("She")
        for i in range(10):
            runner3.walk()
            runner4.run()
        self.assertNotEqual(runner3.distance, runner4.distance)


# ====================================================================================

# Тема "Методы Юнит-тестирования    (tests_12_2)

class Runners:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[self.full_distance / participant.speed] = participant.name
                    self.participants.remove(participant)
        finishers = dict(sorted(finishers.items()))
        return finishers


# ==============================================================
class TournamentTest(unittest.TestCase):
    is_frozen = True  # новый аттрибут

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run1 = Runners("Усэйн", 10)
        self.run2 = Runners("Андрей", 9)
        self.run3 = Runners("Ник")

    @classmethod
    def tearDownClass(cls):
        print()

    def test_first_tournament(self):
        self.func(Tournament(90, self.run3, self.run1), ind=1)

    def test_second_tournament(self):
        self.func(Tournament(90, self.run3, self.run2), ind=2)

    def test_third_tournament(self):
        self.func(Tournament(90, self.run2, self.run3, self.run1), ind=3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def func(self, tournament, ind):
        result = tournament.start()
        loser = result.get(max(result.keys()))
        self.assertTrue(loser == 'Ник')
        self.all_results[ind] = result


if __name__ == '__main__':
    unittest.main()
