from sqlalchemy import BinaryExpression, and_

from domain.entities.queries import UserQuery
from infrastructure.database.filter.base import BaseFilter


class UserFilter(BaseFilter):
    """Filter for users."""

    def where(self, query: UserQuery) -> BinaryExpression | None:
        """Creates a where clause for a user query.

        :param query: The user query.
        :type query: UserQuery
        :returns: A where clause for a user query.
        :rtype: BinaryExpression | None
        """
        if query.name__like:
            return and_(
                self._model.first_name.ilike(f'%{query.name__like}%')
                | self._model.last_name.ilike(f'%{query.name__like}%')
            )
        return None
