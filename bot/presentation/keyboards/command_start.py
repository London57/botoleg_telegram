from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


categories = ["Работа", "Магазин", "Настройки"]


def get_start_keyboard() -> ReplyKeyboardMarkup:
	keyboard = ReplyKeyboardMarkup(
		keyboard=[
			[
				KeyboardButton(text=category) for category in categories
			]
		],
		resize_keyboard=True
	)
	return keyboard