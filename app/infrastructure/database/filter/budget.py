from sqlalchemy import BinaryExpression, and_

from domain.entities.queries import BudgetQuery, CategoryQuery
from infrastructure.database.filter.base import BaseFilter


class BudgetFilter(BaseFilter):
    """Filter for budgets."""

    def where(self, query: BudgetQuery) -> BinaryExpression | None:
        """Creates a where clause for a budget query.

        :param query: The budget query.
        :type query: BudgetQuery
        :returns: A where clause for a budget query.
        :rtype: BinaryExpression | None
        """
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


class CategoryFilter(BaseFilter):
    """Filter for categories."""

    def where(self, query: CategoryQuery) -> BinaryExpression | None:
        """Creates a where clause for a category query.

        :param query: The category query.
        :type query: CategoryQuery
        :returns: A where clause for a category query.
        :rtype: BinaryExpression | None
        """
        if query.name__like:
            return and_(self._model.name.ilike(f'%{query.name__like}%'))

        return None
