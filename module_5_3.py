# Цель: применить знания о перегурзке арифметических операторов и операторов сравнения

# Задача "Нужно больше этажей"

class House:
    def __init__(self, name, number):
        self.name = name
        self.number_of_floors = number

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей {self.number_of_floors}')

    def __eq__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors == other.number_of_floors


    def __lt__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int) or isinstance(value, House):
            self.number_of_floors = self.number_of_floors + value
            return self

    def __sub__(self, value):
        if isinstance(value, int) or isinstance(value, House):
           self.number_of_floors = self.number_of_floors - value
           return self

    def __isub__(self, value):
        if isinstance(value, int) or isinstance(value, House):
           self.number_of_floors = self.number_of_floors - value
           return self


    def __iadd__(self, value):
        if isinstance(value, int) or isinstance(value, House):
            self.number_of_floors = self.number_of_floors + value
            return self

    def __radd__(self, value):
        if isinstance(value, int) or isinstance(value, House):
            self.number_of_floors = self.number_of_floors + value
            return self

    def __mul__(self, value):
        if isinstance(value, int) or isinstance(value, House):
            self.number_of_floors = self.number_of_floors * value
            return self

    def __imul__(self, value):
        if isinstance(value, int) or isinstance(value, House):
            self.number_of_floors = self.number_of_floors * value
            return self





h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
#__eq__
print(h1 == h2)
#__add__
h1 = h1 + 20
print(h1)
#__iadd__
h1 += 10
print(h1)
#__radd__
h2 = 10 + h2
print(h2)
#__sub__
h1 = h1 - 5
print(h1)
#__isub__
h2 -= 5
print(h2)
#__mul__
h1 = h1 * 2
print(h1)
#__imul__
h2 *= 3
print(h2)


print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__





