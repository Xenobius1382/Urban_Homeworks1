# Цели: Применить сокрытие атрибутов и повторить наследование. Рассмотреть на примере объекта из реального мира

# Задача "Изменять нельзя получать"

class Vehicle:

    __COLOR_VARIANTS= ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        return (self.get_model(), self.get_horsepower(), self.get_color(), print(f'Владелец: {self.owner}'))

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print("Нельзя сменить цвет на", new_color)

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5



# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Иван', 'Kia Optima', 'white', 180)


# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Макс'

# Проверяем что поменялось
vehicle1.print_info()