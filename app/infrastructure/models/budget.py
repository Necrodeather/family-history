from __future__ import annotations

from sqlalchemy.orm import Mapped, relationship

from .mixins import BaseMixin, CreatedAtMixin, UpdatedAtMixin
from app.infrastructure.base import str_128, date_sql, decimal

class Category(BaseMixin, CreatedAtMixin, UpdatedAtMixin):
    __abstract__ = True

    name: Mapped[str_128]


class ExpensesCategory(Category):
    __tablename__ = "expenses_categories"

    expenses: Mapped[list["Expenses"]] = relationship(back_populates="category")


class IncomesCategory(Category):
    __tablename__ = "incomes_categories"

    incomes: Mapped[list["Income"]] = relationship(back_populates="category")


class Expenses(BaseMixin, CreatedAtMixin, UpdatedAtMixin):
    __tablename__ = "expenses"

    name: Mapped[str_128]
    category_id: Mapped[int]
    amount: Mapped[decimal]
    date: Mapped[date_sql]
    category: Mapped["ExpensesCategory"] = relationship(back_populates="expenses")


class Income(BaseMixin, CreatedAtMixin, UpdatedAtMixin):
    __tablename__ = "incomes"

    name: Mapped[str_128]
    amount: Mapped[decimal]
    category_id: Mapped[int]
    date: Mapped[date_sql]
    category: Mapped["IncomesCategory"] = relationship(back_populates="incomes")
