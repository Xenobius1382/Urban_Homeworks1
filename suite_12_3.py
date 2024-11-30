# Домашнее задание по теме "Систематизация и пропуск тестов"

# Цель: понять на практике как объединять тесты при помощи TestSuite. Научиться пропускать тесты при помощи встроенных
# в unittest декораторов

# Задача "Заморозка кейсов"

import unittest
import tests_12_1, tests_12_2

tour_ts = unittest.TestSuite()
tour_ts.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
tour_ts.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tour_ts)


