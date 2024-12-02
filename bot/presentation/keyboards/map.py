from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

def get_inline_kbd(tg_user_id) -> InlineKeyboardMarkup:
	url_map = f"{os.getenv("backend_url")}/maps?user_id={tg_user_id}"
	inline_btn = InlineKeyboardButton(text="Открыть карту", url=url_map)
	return InlineKeyboardMarkup(inline_keyboard=[[inline_btn]])