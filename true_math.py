# функция деления на ноль по правилам высшей математики

from math import inf
def divide(first, second):
    if second == 0:
        return inf
    else:
        return first / second

result = divide(40,0)
print(result)