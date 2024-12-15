from application.interfaces.repositories.business import IBusinessRepository

from infrastructure.dbs.postgresql.models import Business
from .base import BaseRepository

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class BusinessRepository(IBusinessRepository, BaseRepository):
	table = Business
	
	async def get_businesses_by_user_id(self, tg_user_id: int, session: AsyncSession):
		print("запрос")
		res = await session.execute(
			  select(self.table).where(
				self.table.owner_id == tg_user_id,
			)
		)
		print(res)
