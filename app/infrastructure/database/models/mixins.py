from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.base import Base, datetime_timezone, uuid_pk


class BaseMixin(Base):
    __abstract__ = True

    id: Mapped[uuid_pk]


class CreatedAtMixin(Base):
    __abstract__ = True

    created_at: Mapped[datetime_timezone] = mapped_column(
        default=datetime_timezone.now
    )


class UpdatedAtMixin(Base):
    __abstract__ = True

    updated_at: Mapped[datetime_timezone] = mapped_column(
        default=datetime_timezone.now,
        onupdate=datetime_timezone.now,
    )
