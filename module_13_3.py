# Домашнее задание по теме "Методы отправки сообщений"

# Цель: написать простейшего телеграм-бота, используя асинхронные функции

# Задача "Он мне ответил!"

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7662349781:AAHJ-LN91qU2CrowQPZbx-ht8byQwcGUG84"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)