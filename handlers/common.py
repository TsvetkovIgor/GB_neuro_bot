import logging
import random
from aiogram import Router, types, F
from aiogram.filters.command import Command
from keyboards.keyboards import keyboard
from utils.random_fox import fox
from utils.random_cat import cat
from aiogram import types


router = Router()

@router.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup=keyboard)


@router.message(Command(commands=['стоп']))
@router.message(Command(commands=['stop']))
async def stop(message: types.Message):
    print(message.from_user.full_name)
    await message.answer(f'Привет, {message.chat.first_name}!')


@router.message(Command(commands=['инфо', 'info']))
@router.message(F.text.lower() == 'инфо')
async def info(message: types.Message):
    print(message.from_user.full_name)
    await message.answer(f'Привет, {message.chat.first_name}!\n '
                         f'Я тестовый бот, созданный в рамках учебной программы "Нейрохищник".\n '
                         f'Автор: студент Цветков И. К.')



@router.message(F.text.lower() == 'покажи лису')
async def info(message: types.Message):
    img_fox = fox()
    await message.answer('Привет, лови лису')
    await message.answer_photo(img_fox)


@router.message(F.text.lower() == 'покажи котика')
async def info(message: types.Message):
    img_cat = cat()
    await message.answer('Привет, лови котика')
    await message.answer_photo(img_cat)


# @router.message(F.text.lower() == 'Законы Мерфи')
# async def info(message: types.Message):
#     with open(merphy.txt, 'r') as file:
#         lines = file.readlines()
#         update.message.reply_text(random.choice(lines))

