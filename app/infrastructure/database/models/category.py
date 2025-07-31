from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.base import str_128, uuid

from .mixins import BaseMixin, CreatedAtMixin, UpdatedAtMixin


class Category(BaseMixin, CreatedAtMixin, UpdatedAtMixin):
    __abstract__ = True

    name: Mapped[str_128] = mapped_column(unique=True)
    user_id: Mapped[uuid] = mapped_column(ForeignKey('user.id'))
    updated_user_id: Mapped[uuid | None] = mapped_column(ForeignKey('user.id'))


class ExpensesCategory(Category):
    __tablename__ = 'expenses_category'

    user: Mapped['User'] = relationship(
        primaryjoin='User.id == ExpensesCategory.user_id'
    )
    updated_user: Mapped['User'] = relationship(
        primaryjoin='User.id == ExpensesCategory.updated_user_id'
    )


class IncomesCategory(Category):
    __tablename__ = 'incomes_category'

    user: Mapped['User'] = relationship(
        primaryjoin='User.id == IncomesCategory.user_id'
    )
    updated_user: Mapped['User'] = relationship(
        primaryjoin='User.id == IncomesCategory.updated_user_id'
    )
