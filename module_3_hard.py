# Дополнительное практическое задание по модулю: "Подробнее о функциях."

# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности

# Задание "Раз, два, три, четыре, пять .... Это не всё?"

def calculate_structure_sum(data_structure):
    numbers = 0
    strings = 0

   # for obj in data_structure:
    def recurse(obj):
        nonlocal numbers, strings
        # Проверка на число
        if isinstance(obj, int):
            numbers += obj
        # Проверка на строку
        elif isinstance(obj, str):
            strings += len(obj)
        # Рекурсивный обход значений словаря
        elif isinstance(obj, dict):
            for key, value in obj.items():
                recurse(key)
                recurse(value)
        # Рекурсивный обход элементов списка
        elif isinstance(obj, list):
            for item in obj:
                recurse(item)
        # Рекурсивный обход элементов кортежа
        elif isinstance(obj, tuple):
            for i in obj:
                recurse(i)
        # Рекурсивный обход элементов множества
        elif isinstance(obj, set):
            for k in obj:
                recurse(k)


    recurse(data_structure)
    return numbers + strings

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
