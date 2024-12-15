from infrastructure.dbs.postgresql.options.db import get_async_session

from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.dbs.postgresql.options.db import async_session_maker


class BaseRepository:
    async def get_async_session(self):
        async with async_session_maker() as session:  # Здесь исправлено
            yield session

    async def init_session(self) -> AsyncSession:
        async for session in self.get_async_session():
            return session
