from aiogram import Router, F
from aiogram.filters import StateFilter, and_f
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from presentation.states.work import WorkStates
from presentation.keyboards.work import categories
from presentation.keyboards.businesses_inline import BusinessInlineKbd

from presentation.keyboards.map import get_inline_kbd
from presentation.messages.work import invalid_work_button_message

from infrastructure.dbs.mongodb.repositories.businesses import BusinessRepository


router = Router()


@router.message(and_f(F.text == "💰бизнес", StateFilter(WorkStates.start_work)))
async def work(message: Message, repo = BusinessRepository()):
	
	user_id = message.from_user.id
	if repo.is_have_business(user_id):
		global business_kbd
		business_kbd = BusinessInlineKbd()
		business_kbd.set_data(repo.get_businesses_by_user_id(user_id))
		
		await message.answer(str(business_kbd.get_data()), reply_markup=business_kbd.get_business_inline_kbd())
	else:
		await message.answer("У вас пока нет бизнесов. Купить их вы можете на карте.", reply_markup=get_inline_kbd(user_id))


async def update_num_text(message: Message):
    await message.edit_text(
			business_kbd.get_data(),
      reply_markup=business_kbd.get_business_inline_kbd()
    )

@router.callback_query(F.data.startswith("business"))
async def callback_business_kbd(callback: CallbackQuery):
	action = callback.data.split("_")[1]

	if action == "next":
		business_kbd.change_index("+")
		await update_num_text(callback.message)
	elif action == "before":
		business_kbd.change_index("-")
		await update_num_text(callback.message)