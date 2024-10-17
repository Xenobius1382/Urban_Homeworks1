# Домашнее задание по теме "Введение в функциональное программирование"

# Цель: научиться обращаться к функциям, как к объекту и передавать их в другие функции для вызова

# Задача "Вызов разом"

def mul_by_4(x):
    res = 0
    for i in x:
        res += i*4
    return res

def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results

print(apply_all_func([1, 10, 34, 15, 9, 2, 51], max, min, mul_by_4))
print(apply_all_func([1, 10, 34, 15, 9, 2, 51], len, sum, sorted))
