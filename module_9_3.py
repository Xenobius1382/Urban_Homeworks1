# Домашнее задание по теме "Генераторные сборки"

# Цель: понять механизм создания генераторных сборок и использования встроенных функций-генераторов

first = ['Strings', 'Student', 'Computers']

second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x[0]) - len(x[1]) for x in zip(first, second) if len(x[0]) != len(x[1]))
print(list(first_result))

second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))
print(list(second_result))






