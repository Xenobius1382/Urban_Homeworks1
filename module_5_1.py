# Цель: применить на практике знания о классах, объектах и их атрибутах

# Задача "Developer - не только разработчик"

class House:
    def __init__(self, name, number):
        self.name = name
        self.number_of_floors = number

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if self.new_floor > self.number_of_floors or self.new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, self.new_floor+1):
                print(i)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)



