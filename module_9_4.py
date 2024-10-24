# Домашнее задание по теме "Создание функций на лету"

# Цель: освоить на практике замыкание, объекты-функторы и lambda-функции

# Задача "Функциональное разнообразие"
import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))

# =================================================================================

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for i in data_set:
                file.write(f'{str(i)}\n')

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#===================================================================================

class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Или', 'Возможно')
print(first_ball())
print(first_ball())
print(first_ball())



