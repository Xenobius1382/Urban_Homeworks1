# Домашнее задание по теме "Блокировки и обработка ошибок"

# Цель: освоить блокировки потоков, используя объекты класса Lock и его методы

# Задача "Банковские операции"

import threading
import time
import random
class Bank:                                                  # создаем класс Bank с двумя методами deposit и take
    lock = threading.Lock()

    def __init__(self):
        self.balance = 0

    def deposit(self):                                       # метод deposit прибавляет к балансу случайное число
                                                             # от 50 до 500 и проверяет, если баланс больше или
        for i in range(100):                                 # равен 500 и замок закрыт - открывает замок
            rand = random.randint(50, 500)
            self.balance += rand
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {rand}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):                                           # метод take минусует с баланса случайное число от 50
                                                              # до 500 и проверяет, если отнимаемое число меньше или
        for i in range(100):                                  # равно балансу - закрывает замок и блокирует переменную
            rand = random.randint(50, 500)              # self.balance
            print(f'Запрос на {rand}')
            if rand <= self.balance:
                self.balance -= rand
                print(f'Снятие: {rand}. Баланс: {self.balance}')
            else:
                print('Запрос отклонен, недостаточно средств')
                self.lock.acquire()

bk = Bank()


th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')







