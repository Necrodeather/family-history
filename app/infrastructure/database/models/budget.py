from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database.base import date_sql, decimal, str_128, uuid

from .mixins import BaseMixin, CreatedAtMixin, UpdatedAtMixin


class Category(BaseMixin, CreatedAtMixin, UpdatedAtMixin):
    __abstract__ = True

    name: Mapped[str_128] = mapped_column(unique=True)


class ExpensesCategory(Category):
    __tablename__ = 'expenses_categories'

    expenses: Mapped[list['Expenses']] = relationship(
        back_populates='category',
    )


class IncomesCategory(Category):
    __tablename__ = 'incomes_categories'

    incomes: Mapped[list['Income']] = relationship(back_populates='category')


class Budget(BaseMixin, CreatedAtMixin, UpdatedAtMixin):
    __abstract__ = True

    name: Mapped[str_128]
    amount: Mapped[decimal]
    date: Mapped[date_sql]


class Expenses(Budget):
    __tablename__ = 'expenses'

    category_id: Mapped[uuid] = mapped_column(
        ForeignKey('expenses_categories.id'),
    )
    category: Mapped['ExpensesCategory'] = relationship(
        back_populates='expenses',
    )


class Income(Budget):
    __tablename__ = 'incomes'

    category_id: Mapped[uuid] = mapped_column(
        ForeignKey('incomes_categories.id'),
    )
    category: Mapped['IncomesCategory'] = relationship(
        back_populates='incomes',
    )
