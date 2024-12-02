from aiogram import Router, F
from aiogram.filters import Filter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from presentation.states.work import WorkStates
from presentation.keyboards.work import get_work_keyboard


router = Router()

@router.message(F.text == "Работа")
async def work(message: Message, state: FSMContext):

	await message.answer(text="Info about you here later", reply_markup=get_work_keyboard())

	await state.set_state(WorkStates.start_work)

