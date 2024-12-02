from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


categories = ["💰бизнес", "дальнобойщик", "таксист"]

def get_work_keyboard() -> ReplyKeyboardMarkup:
	keyboard = ReplyKeyboardMarkup(
		keyboard=[
			[
				KeyboardButton(text=category) for category in categories
			]
		],
		resize_keyboard=True
	)
	return keyboard