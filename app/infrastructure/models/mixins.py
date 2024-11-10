from datetime import datetime
from sqlalchemy.orm import Mapped

from app.infrastructure.base import Base, uuid_pk

class BaseMixin(Base):
    __abstract__ = True

    id: Mapped[uuid_pk]


class CreatedAtMixin(Base):
    __abstract__ = True

    created_at: Mapped[datetime]


class UpdatedAtMixin(Base):
    __abstract__ = True

    updated_at: Mapped[datetime]
