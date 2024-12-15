# from bot.infrastructure.db.models.friends import Friend
from infrastructure.dbs.postgresql.options.db import engine, Base

async def create_tables():
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.create_all)