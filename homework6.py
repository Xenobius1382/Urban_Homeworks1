# Практическое задание по теме: "Словари и множества"

# Работа со словарями

my_dict = {'Max': 2000, 'Dima': 2005, 'Alex': 2010}
print(my_dict)
print(my_dict['Dima'])
print(my_dict.get('Andrey'))
my_dict.update({'Olya': 1990, 'Tanya': 1995})
One_of_pairs = my_dict.pop('Max')
print(One_of_pairs)
print(my_dict)

# Работа с множествами

my_set_ = {1,2,3,2,2,3,1,'Inna', True, 1, 'Max', 2, 'Inna', True, 'Max',3,3,2}
print(my_set_)
my_set_.add(5)
my_set_.add(False)
print(my_set_)
my_set_.remove(1)
print(my_set_)




