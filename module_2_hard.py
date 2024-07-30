# Дополнительное практическое задание по модулю: "Основные операторы"

# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности

# Задание "Слишком древний шифр"

result = []
def Indiana_Jones(code):
    for i in range(1, code):
        for j in range(2, code):
            if (i + j) == code or (code % (i + j)) == 0:
                if (f'{j}+{i}') not in result:
                    result.append(f'{i}+{j}')

    return result

Indiana_Jones(13)
print(result)


