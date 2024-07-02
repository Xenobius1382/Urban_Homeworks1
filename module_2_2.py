# применение навыков создания условных конструкций и знания операторов if, else, elif / and, or, not.

# создаем три переменные куда будут сохраняться числа, которые ввел пользователь для проверки

first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

# пишем конструкцию условия для проверки и выводим результат

if first == second and second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
elif not first == second and not first == third and not second == third:
    print(0)
