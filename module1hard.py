# Дополнительное практическое задание по модулю: "Базовые структуры данных."

grades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(list(students)) # преобразуем множество в список и сразу сортируем его

# находим среднее арифметичсекое каждого элемента списка и записываем это значение вместо первоначального

grades[0] = sum(grades[0])/len(grades[0])
grades[1] = sum(grades[1])/len(grades[1])
grades[2] = sum(grades[2])/len(grades[2])
grades[3] = sum(grades[3])/len(grades[3])
grades[4] = sum(grades[4])/len(grades[4])

#объеденяем два списка в словарь

srednyii_ball = dict(zip(students, grades))
print(srednyii_ball)

