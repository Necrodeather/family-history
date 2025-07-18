from sqlalchemy import BinaryExpression, and_

from app.domain.entities.budget import BudgetQuery
from app.domain.entities.category import CategoryQuery
from app.infrastructure.database.models.budget import (
    Expenses,
    ExpensesCategory,
    Income,
    IncomesCategory,
)
from app.infrastructure.database.repository.filter.base import SqlAlchemyFilter


class BudgetFilter(SqlAlchemyFilter):
    def where(self, query: BudgetQuery) -> BinaryExpression | None:
        and_args = []
        if query.name__like:
            and_args.append(self._model.name.ilike(f'%{query.name__like}%'))
        if query.category_id:
            and_args.append(self._model.category_id == query.category_id)
        if query.user_id:
            and_args.append(self._model.user_id == query.user_id)

        if and_args:
            return and_(*and_args)

        return None


class CategoryFilter(SqlAlchemyFilter):
    def where(self, query: CategoryQuery) -> BinaryExpression | None:
        if query.name__like:
            return and_(self._model.name.ilike(f'%{query.name__like}%'))

        return None


income_filter = BudgetFilter(Income)
expenses_filter = BudgetFilter(Expenses)

income_category_filter = CategoryFilter(IncomesCategory)
expenses_category_filter = CategoryFilter(ExpensesCategory)
