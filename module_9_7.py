# Домашнее задание по теме "Декораторы"

# Цель задания: Освоить механизмы создания декораторов Python.
# Практически применить знания, создав функцию декоратор и обернув ею другую функцию.


def is_prime(func):         # создаем декоратор
    def wrapper(*args, **kwargs):
        cnt = 0
        res = func(*args, **kwargs)
        for i in range(2, res // 2 + 1):
            if res % i == 0:
                cnt += 1
        if cnt <= 0:
            return f'{res} - Число простое'
        else:
            return f'{res} - Число составное'
    return wrapper

# применяем декоратор к функции
@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(7, 8 ,2)
print(result)


