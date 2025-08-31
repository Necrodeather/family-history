from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.base import Base, datetime_timezone, uuid_pk


class BaseMixin(Base):
    """Base mixin for all models."""
    __abstract__ = True

    id: Mapped[uuid_pk]


class CreatedAtMixin(Base):
    """Mixin for created_at timestamp."""
    __abstract__ = True

    created_at: Mapped[datetime_timezone] = mapped_column(
        default=datetime_timezone.now
    )


class UpdatedAtMixin(Base):
    """Mixin for updated_at timestamp."""
    __abstract__ = True

    updated_at: Mapped[datetime_timezone] = mapped_column(
        default=datetime_timezone.now,
        onupdate=datetime_timezone.now,
    )
