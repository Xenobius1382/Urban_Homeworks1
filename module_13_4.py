# Домашнее задание по теме "Машина состояний"

# Цель: получить навык работы с состояниями в телеграм-боте

# Задача "Цепочка вопросов"

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text='Calories')
async def set_age(message):
    await message.answer('Введите свой возраст')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост')
    await UserState.growth.set()



@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    date = await state.get_data()
    await message.answer(f'Ваша норма калорий {(10 * int(date["weight"])) + 6.25 * int(date["growth"]) - (5 * int(date["age"])) + 5 }')
    await state.finish()



@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')



@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


