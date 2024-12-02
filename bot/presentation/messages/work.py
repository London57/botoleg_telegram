from .invalid_button import invalid_button_message

def invalid_work_button_message(tg_username: str) -> str:
	invalid_button_message(f"{tg_username}, выбери работу, на которой хочешь сейчас поработать.")