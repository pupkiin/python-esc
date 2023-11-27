# как я понял, файл с обработчиками ^^)

from aiogram import Router, F, types
from aiogram.types import Message
from aiogram.filters import Command

import kb
import text

router = Router()

@router.message(F.text, Command("start")) # декоратор? - почитать
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)
