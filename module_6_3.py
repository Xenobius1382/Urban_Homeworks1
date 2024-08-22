# Цель: закрепить знания множественного наследования в Python

# Задача "Мифическое наследование"

class Horse:

    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance

class Eagle:

    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance

class Pegasus(Eagle, Horse):

    def __init__(self):
        super().__init__()
        Horse.__init__(self)


    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def move(self, dy, dx):
        self.run(dx)
        self.fly(dy)


    def voice(self):
        super().__init__()
        print(self.sound)



p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
