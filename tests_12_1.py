# Домашнее задание по теме "Простые Юнит-Тесты"

# Цель: приобрести навык создания простейших Юнит-тестов

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
    def test_walk(self):
        man = Runner('Max')
        for _ in range(10):
            man.walk()
        self.assertEqual(man.distance, 50)

    def test_run(self):
        man = Runner('Max')
        for _ in range(10):
            man.run()
        self.assertEqual(man.distance, 100)

    def test_challenge(self):
        man = Runner('Max')
        boy = Runner('Alex')
        for _ in range(10):
            man.run()
        for _ in range(10):
            boy.walk()
        self.assertNotEqual(man.distance, boy.distance)


if __name__ == '__main__':
    unittest.main()






