from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from presentation.keyboards.command_start import get_start_keyboard


router = Router()

@router.message(CommandStart())
async def start(message: Message):
	await message.answer(text="Info about you here later", reply_markup=get_start_keyboard())