# Домашнее задание по теме "Создание исключений"

# Цель: освоить навык создания пользовательских исключений и использовать его в решении задачи. Повторить тему ООП и
# принцип инкапсуляции

# Задача "Некорректность"

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers
        self.__is_valid_numbers(__numbers)
        self.__is_valid_vin(__vin)

    def __is_valid_vin(self, __vin):
        self.__vin = __vin
        if isinstance(__vin, int) == False:
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not 1000000 <= __vin <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True
    def __is_valid_numbers(self, __numbers):
        if not isinstance(__numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(__numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True

try:
   first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')
try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')

