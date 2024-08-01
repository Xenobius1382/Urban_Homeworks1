# фнукция деления на ноль по правилам школьной математики
def divide(first, second):
    if second == 0:
        return 'Ошибка'
    else:
        return first / second

result = divide(30,0)
print(result)


