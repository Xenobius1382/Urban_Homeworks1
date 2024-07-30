# Цель: применить знания о рекурсии в решении задачи

# Задача "Рекурсивное умножение цифр"

def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if not ((len(str_number)) > 1):
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(506045)
print(result)



