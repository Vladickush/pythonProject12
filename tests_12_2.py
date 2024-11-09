# Тема "Методы Юнит-тестирования
import unittest
import pprint


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    """  Эти методы не вызываются и я их закоментировал
    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name
    """


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

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        pprint.pprint(cls.all_results)

    def test_1(self):
        race = Tournament(90, self.nick, self.usain)
        result = race.start()
        loser = result.get(max(result.keys()))
        self.assertTrue(loser == 'Ник')
        self.all_results[1] = result

    def test_2(self):
        race = Tournament(90, self.nick, self.andrey)
        result = race.start()
        loser = result.get(max(result.keys()))
        self.assertTrue(loser == 'Ник')
        self.all_results[2] = result

    def test_3(self):
        race = Tournament(90, self.andrey, self.nick, self.usain)
        result = race.start()
        loser = result.get(max(result.keys()))
        self.assertTrue(loser == 'Ник')
        self.all_results[3] = result

if __name__ == '__main__':
    unittest.main()



