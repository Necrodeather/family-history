from sqlalchemy import select

from app.domain.entities.user import UserCreate, UserUpdate
from app.infrastructure.database.models.user import User
from app.infrastructure.database.repository.crud.base import (
    SQLAlchemyCRUDRepository,
)


class CRUDAuth(SQLAlchemyCRUDRepository[User, UserCreate, UserUpdate]):
    async def get_user_by_email(self, email: str) -> User:
        stmt = select(User).where(User.email == email)
        result = await self.session.execute(stmt)
        return result.scalar()


class CRUDUser(SQLAlchemyCRUDRepository[User, UserCreate, UserUpdate]):
    pass


auth_crud = CRUDAuth(User)
user_crud = CRUDUser(User)
