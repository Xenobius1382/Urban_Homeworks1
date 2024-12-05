# Домашнее задание по теме "Асинхронность на практике"

# Цель: приобрести навык использования асинхронного запуска функций на практике

# Задача "Асинхронные силачи"

import time
import asyncio

async def start_strongman(name, power):
        print(f'Силач {name} начал соревнования')
        for _ in range(1, 6):
            print(f'Силач {name} поднял шар {_}')
            await asyncio.sleep(1/power)
        print(f'Силач {name} закончил соревнования')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Schwarz', 150))
    task2 = asyncio.create_task(start_strongman('Ivan', 30))
    task3 = asyncio.create_task(start_strongman('Hafthor', 10))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())




