from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.base import date_sql, decimal, str_128, uuid

from .mixins import BaseMixin, CreatedAtMixin, UpdatedAtMixin


class Budget(BaseMixin, CreatedAtMixin, UpdatedAtMixin):
    """Base class for all budget models."""
    __abstract__ = True

    name: Mapped[str_128]
    amount: Mapped[decimal]
    date: Mapped[date_sql]
    user_id: Mapped[uuid] = mapped_column(ForeignKey('user.id'))
    updated_user_id: Mapped[uuid | None] = mapped_column(ForeignKey('user.id'))


class Expenses(Budget):
    """Model for expenses."""
    __tablename__ = 'expenses'

    category_id: Mapped[uuid] = mapped_column(
        ForeignKey('expenses_category.id'),
    )
    user: Mapped['User'] = relationship(
        primaryjoin='User.id == Expenses.user_id'
    )
    updated_user: Mapped['User'] = relationship(
        primaryjoin='User.id == Expenses.updated_user_id'
    )


class Income(Budget):
    """Model for income."""
    __tablename__ = 'income'

    category_id: Mapped[uuid] = mapped_column(
        ForeignKey('incomes_category.id'),
    )
    user: Mapped['User'] = relationship(
        primaryjoin='User.id == Income.user_id'
    )
    updated_user: Mapped['User'] = relationship(
        primaryjoin='User.id == Income.updated_user_id'
    )
