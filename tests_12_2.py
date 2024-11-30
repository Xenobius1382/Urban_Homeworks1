# Домашнее задание по теме "Методы Юнит-тестирования"
import unittest


# Цель: освоить методы, которые содержит класс TestCase

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        # Создаем атрибут класса all_results
        cls.all_results = {}

    def setUp(self):
        # Создаем объекты бегунов
        self.usain = Runner("Usain", 10)
        self.andrey = Runner("Andrey", 9)
        self.nick = Runner("Nick", 3)
    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_usain_vs_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        last_runner = max(results.keys())
        self.assertEqual(results[last_runner].name, 'Nick')
        self.__class__.all_results['usain_vs_nick'] = results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_andrey_vs_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        last_runner = max(results.keys())
        self.assertEqual(results[last_runner].name, 'Nick')
        self.__class__.all_results['andrey_vs_nick'] = results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_andrey_vs_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        last_runner = max(results.keys())
        self.assertEqual(results[last_runner].name, 'Nick')
        self.__class__.all_results['usain_andrey_vs_nick'] = results

    @classmethod
    def tearDownClass(cls):
        # Преобразование значений словаря в имена участников
        formatted_results = {}
        for key, value in cls.all_results.items():
            new_value = {}
            for k, v in value.items():
                new_value[k] = v.__str__()
            formatted_results[key] = new_value

        # Вывод результатов
        for key, value in formatted_results.items():
            print(f"{key}: {value}")
