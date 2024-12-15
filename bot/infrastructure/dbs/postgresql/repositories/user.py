from application.interfaces.repositories.user import IUserRepository

from infrastructure.dbs.postgresql.models import User
from .base import BaseRepository

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class UserRepository(IUserRepository, BaseRepository):
	table = User
	
	async def is_have_business(self, tg_user_id: int, session: AsyncSession):
		data = await session.execute(
				select(self.table.businesses).where(
				self.table.telergram_id == tg_user_id
			)
		)
		
		print("data", data)
		if data:
			return True