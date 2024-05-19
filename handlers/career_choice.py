from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.career_keyboard import make_keyboard


router = Router()


available_jobs = [
    'Программист',
    'Маркетолог',
    'Менеджер',
    'Аналитик',
    'Бухгалтер'
]
available_grades = [
    'Низкий',
    'Средний',
    'Высокий'
]
available_checks = [
    'меньше 100 т.р',
    '100 т.руб',
    'больше 100 т.р'
]


class Choice(StatesGroup):
    job = State()
    grade = State()
    check = State()


@router.message(Command(commands=['prof']))
async def start(message: types.Message, state: FSMContext):
    await message.answer('Какая профессия вас интересует?', reply_markup=make_keyboard(available_jobs))
    await state.set_state(Choice.job)


@router.message(Choice.job, F.text.in_(available_jobs))
async def jobs(message: types.Message, state: FSMContext):
    await message.answer('Как вы оцениваете свою профессию?', reply_markup=make_keyboard(available_grades))
    await state.set_state(Choice.grade)


@router.message(Choice.job)
async def job_incorrectly(message: types.Message):
    await message.answer('Неправильно. Попробуйте ещё раз', reply_markup=make_keyboard(available_jobs))


@router.message(Choice.grade, F.text.in_(available_grades))
async def grates(message: types.Message, state: FSMContext):
    await  message.answer('Как вы оцениваете свой средний чек?', reply_markup=make_keyboard(available_checks))
    await state.set_state(Choice.check)


@router.message(Choice.grade)
async def grate_incorrectly(message: types.Message):
    await message.answer('Неправильно. Попробуйте ещё раз', reply_markup=make_keyboard(available_grades))


@router.message(Choice.check, F.text.in_(available_checks))
async def check(message: types.Message, state: FSMContext):
    await message.answer(f'Вы всё прошли, с вами свяжутся наши hr!',
                         reply_markup=types.ReplyKeyboardRemove())
    await state.clear()


@router.message(Choice.check)
async def check_incorrectly(message: types.Message):
    await message.answer('Неправильно. Попробуйте ещё раз', reply_markup=make_keyboard(available_checks))
