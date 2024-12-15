from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from uuid import UUID

from infrastructure.dbs.postgresql.options.db import Base
from domain.businesses.business_types import Business_types

from sqlalchemy import Enum as sqlalchemy_enum

class Business(Base):
	__tablename__ = "businesses"
	type = mapped_column(sqlalchemy_enum(Business_types))
	level: Mapped[int]
	owner_id: Mapped[UUID] = ForeignKey("users.id")
	owner = relationship("User", back_populates="business")