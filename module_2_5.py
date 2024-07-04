# закрепление навыков написания функций и их вызовов


def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for k in range(m):
            matrix[i].append(value)
    return matrix
result_1 = get_matrix(8, 5, 6)
result_2 = get_matrix(3, 7, 2)
result_3 = get_matrix(5, 9, 23)
print(result_1)
print(result_2)
print(result_3)