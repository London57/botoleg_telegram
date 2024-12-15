from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from uuid import UUID

from infrastructure.dbs.postgresql.options.db import Base


class User(Base):
	__tablename__ = "users"
	telergram_id: Mapped[int]
	telegram_username: Mapped[str]
	balance: Mapped[int]
	businesses: Mapped[list[int]] = ForeignKey("businesses.id")
	business_table_relastionship = relationship("Business", back_populates="user")

