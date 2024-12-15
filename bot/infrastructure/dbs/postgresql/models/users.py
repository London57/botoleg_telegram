from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from uuid import UUID

from infrastructure.dbs.postgresql.options import Base


class User(Base):
	__tablename__ = "users"
	telergram_id: Mapped[int]
	telegram_username: Mapped[str]
	balance: Mapped[int]
	businesses: Mapped[list[int]] # businesses_ids

