# Домашнее задание по теме "Try и Except"

# Задание "Программистам всё можно"


def add_everything_up(a, b):
    try:
        return print(a + b)
    except TypeError:
        c = str(a) + str(b)
        print(c)


add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)


