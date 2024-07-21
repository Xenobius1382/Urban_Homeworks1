# Домашнее задание по уроку "Распаковка позиционных параметров"
# Цель задания: Освоить создание функций с параметрами по умолчанию и практику вызова этих функций
# с различным количеством аргументов


# 1.Функция с параметрами по умолчанию:

def print_params( a = 1, b = 'Word', c = True):
    print(a, b, c)

print_params()
print_params(a = 3)
print_params(b = 'String')
print_params(a = 5, c = 'False')
print_params(b = 25)
print_params(c = [1,2,3])

# 2.Распаковка параметров:

values_list = [6, 'Apple', True]
values_dict = {'a': 8, 'b': 'Table', 'c': False}

print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:

values_list_2 = ['Cup', 65]
print_params(*values_list_2, 42)



