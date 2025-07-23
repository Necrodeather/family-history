from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.domain.entities.user import UserCreate, UserUpdate
from app.domain.exceptions import UserAlreadyRegisteredError
from app.infrastructure.database.models.user import User
from app.infrastructure.database.repository.crud.base import (
    SQLAlchemyCRUDRepository,
)
from app.infrastructure.database.repository.filter.user import user_filter


class CRUDAuth(SQLAlchemyCRUDRepository[User, UserCreate, UserUpdate]):
    async def get_user_by_email(self, email: str) -> User:
        stmt = select(User).where(User.email == email)
        result = await self.session.execute(stmt)
        return result.scalar()

    async def create(self, object: UserCreate) -> User:
        try:
            return await super().create(object)
        except IntegrityError:
            raise UserAlreadyRegisteredError()


class CRUDUser(SQLAlchemyCRUDRepository[User, UserCreate, UserUpdate]):
    pass


auth_crud = CRUDAuth(User, user_filter)
user_crud = CRUDUser(User, user_filter)
