from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from uuid import UUID

from infrastructure.dbs.postgresql.options import Base

from domain.businesses.business_types import Business_types

class Business(Base):
	__tablename__ = "businesses"
	type: ...
	level: Mapped[int]
	owner_id: Mapped[UUID] = relationship("User", back_populates="business")