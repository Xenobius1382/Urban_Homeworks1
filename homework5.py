# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"

tuple_ = 1,2,3, 'String', False
immutable_var = tuple_
print(immutable_var)
# tuple_[0] = 100  кортеж относится к неизменяемым типам данных и не поддерживает обращение по элементам

colours = ['red','blue','orange']
mutable_list = colours
colours[0] = 'black'
colours[2] = 'red'
print(mutable_list)