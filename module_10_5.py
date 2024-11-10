# Домашнее задание по теме "Многопроцессное программирование"

# Цель: понять разницу между линейным и многопроцессным подходом, выполнив операции обоими способами

# Задача "Многопроцессное считывание"

from multiprocessing import Pool
import time


def read_info(name):
    all_data = []

    # Открываем файл для чтения
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line.strip():
                break
            all_data.append(line)




if __name__ == "__main__":

    filenames = [f'./file {i}.txt' for i in range(1, 5)]

    # Линейный вызов
    start_time = time.time()

    for name in filenames:
        read_info(name)

    end_time = time.time()
    print(f"{end_time - start_time:.6f} (линейный)")

    # Многопроцессный вызов
    start_time = time.time()

    with Pool() as pool:
        pool.map(read_info, filenames)

    end_time = time.time()
    print(f"{end_time - start_time:.6f} (многопроцессный)")
    
