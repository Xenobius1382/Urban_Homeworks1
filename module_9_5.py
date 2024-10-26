# Домашнее задание по теме "Итераторы"

# Цель: освоить механизмы работы итераторов и описания методов __next__ и __iter__. Закрепить навык создания и
# выбрасывания исключений

# Задача "Range - это просто"

class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        if self.step == 0:
            raise StepValueError()
        if self.start > self.stop and self.step > 0:
            raise StepValueError()

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        value = self.pointer
        if self.step > 0:
            if self.pointer > self.stop:
                raise StopIteration()
        else:
            if self.pointer < self.stop:
                raise StopIteration()
        self.pointer += self.step
        return value


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()

try:
    iter5 = Iterator(10, 1)
    for i in iter5:
        print(i, end=' ')
except StepValueError:
    print('Начальное значение больше конечного, нужен отрицательный шаг')

