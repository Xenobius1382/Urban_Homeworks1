# Цель: применить базовые знания о наследовании классов для решения задачи

# Задача "Съедобное, несъедобное"

class Animal:

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:

    def __init__(self, name):
        self.name = name
        self.edible = False


class Flower(Plant):
    pass


class Fruit(Plant):
   pass

class Mammal(Animal):
    pass

class Predator(Animal):
    pass



a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
p2.edible = True

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)






