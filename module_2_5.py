# закрепление навыков написания функций и их вызовов


def get_matrix(n, m, value):          # создаем функцию которая будет заполнять матрицу
    matrix = []                       # создаем пустой список
    for i in range(n):
        matrix.append([])             # заполняем созданный список пустыми списками формирующими матрицу в количестве n
        for k in range(m):
            matrix[i].append(value)   # заполняем добавленные списки значениями value в количестве m
    return matrix
result_1 = get_matrix(8, 5, 6)  # вызываем функцию и передаем ей значения
result_2 = get_matrix(3, 7, 2)
result_3 = get_matrix(5, 9, 23)
print(result_1)                              # выводим результат в консоль
print(result_2)
print(result_3)