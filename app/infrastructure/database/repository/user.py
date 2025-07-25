from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.domain.entities.user import UserCreate, UserUpdate
from app.domain.exceptions import UserAlreadyRegisteredError
from app.infrastructure.database.models.user import User
from app.infrastructure.database.repository.base import (
    BaseRepository,
)


class AuthRepository(BaseRepository[User, UserCreate, UserUpdate]):
    async def get_user_by_email(self, email: str) -> User:
        stmt = select(User).where(User.email == email)
        async with self._engine.session() as session:
            result = await session.execute(stmt)
        return result.scalar()

    async def create(self, object: UserCreate) -> User:
        try:
            return await super().create(object)
        except IntegrityError:
            raise UserAlreadyRegisteredError()


class UserRepository(BaseRepository[User, UserCreate, UserUpdate]):
    pass
