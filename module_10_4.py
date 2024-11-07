# Домашнее задание по теме "Очереди для обмена данными между потоками."

# Цель: Применить очереди в работе с потоками, используя класс Queue

# Задача "Потоки гостей в кафе"

import threading
import time
import random
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:

    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f"{guest.name} сел за стол номер {table.number}")

            else:
                self.queue.put(guest)
                print(f"{guest.name} встал в очередь")

    def discuss_guests(self):
        while any(table.guest is not None for table in self.tables) or not self.queue.empty():
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушел(ушла)")
                    print(f"Стол номер {table.number} освободился")
                    table.guest = None
            if not self.queue.empty() and table.guest is None:
                new_guest = self.queue.get()
                table.guest = new_guest
                new_guest.start()
                print(f"{new_guest.name} вышел из очереди и сел за стол {table.number}")


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()









