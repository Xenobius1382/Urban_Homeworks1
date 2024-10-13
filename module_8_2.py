# Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции"

# Цель: понять как работают исключения внутри функций и как обрабатываются эти исключения на практике при
# помощи try-except

# Задача "План перехват"


def personal_sum(numbers):
    global incorrect_data
    incorrect_data = 0
    result = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            print('Некорректный тип данных')
            incorrect_data += 1
    return (result, incorrect_data)


def calculate_average(numbers):
    try:
        global incorrect_data
        total = personal_sum(numbers)
        cnt = len(numbers) - incorrect_data
        avrg = total[0] / cnt
        return avrg
    except ZeroDivisionError:
        print('Нет чисел для подсчета')
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None



print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
