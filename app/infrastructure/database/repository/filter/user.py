from sqlalchemy import BinaryExpression, and_

from app.domain.entities.user import UserQuery
from app.infrastructure.database.models.user import User
from app.infrastructure.database.repository.filter.base import SqlAlchemyFilter


class UserFilter(SqlAlchemyFilter):
    def where(self, query: UserQuery) -> BinaryExpression | None:
        if query.name__like:
            return and_(
                self._model.first_name.ilike(f'%{query.name__like}%')
                | self._model.last_name.ilike(f'%{query.name__like}%')
            )
        return None


user_filter = UserFilter(User)
