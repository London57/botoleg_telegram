from aiogram import Dispatcher, Bot
from aiogram.types import Message
from aiogram.filters import Command
import asyncio
from presentation.routes.routers import routers

from infrastructure.dbs.postgresql.options.create_tables import create_tables

bot = Bot(token="7207325779:AAF8Msg2WNW2oqI9JbCk8TTDz6xGIKQ3wYM")


dp = Dispatcher()
dp.include_routers(*routers)

async def main():
	await create_tables()
	await dp.start_polling(bot)

asyncio.run(main())