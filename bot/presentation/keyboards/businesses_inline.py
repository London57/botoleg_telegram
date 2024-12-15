from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class BusinessInlineKbd:
	index = 0
	def set_data(self, data: list) -> None:
			self.data = data
											
	def change_index(self, char: str) -> None:
			if char == "+":
				if len(self.data) == self.index + 1:
					self.index = 0
				else:
					self.index += 1
			elif char == "-":
				if self.index == 0:
					self.index = len(self.data) - 1
				else:
					self.index -= 1

	def get_data(self) -> str:
		import base64
		business_data: dict = self.data[self.index]

		return f"{business_data.get("city")}, {business_data.get("business_name")}"
	

	def get_detail_data(self):
		...

	def get_business_inline_kbd(self) -> InlineKeyboardMarkup:
		if len(self.data) > 1:
			return InlineKeyboardMarkup(
				inline_keyboard=[
					[
						InlineKeyboardButton(text="before", callback_data="business_before"),
						InlineKeyboardButton(text="next", callback_data="business_next"),
					],
					[
						InlineKeyboardButton(text="Управлять", callback_data="business_manage")
					]
				]
			)
