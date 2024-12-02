from aiogram.fsm.state import State, StatesGroup

from presentation.keyboards.work import categories

class WorkStates(StatesGroup):
	start_work = State()