from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from domain.entities.user import UserCreate, UserUpdate
from domain.exceptions import UserAlreadyRegisteredError
from infrastructure.database.models.user import User
from infrastructure.database.repository.base import (
    BaseRepository,
)


class AuthRepository(BaseRepository[User, UserCreate, UserUpdate]):
    """Repository for authentication."""

    async def get_user_by_email(self, email: str) -> User:
        """Gets a user by their email.

        :param email: The user's email.
        :type email: str
        :returns: The user, or None if they do not exist.
        :rtype: User
        """
        stmt = select(User).where(User.email == email)
        async with self._engine.session() as session:
            result = await session.execute(stmt)
        return result.scalar()

    async def create(self, object: UserCreate) -> User:
        """Creates a new user.

        :param object: The data to create the user with.
        :type object: UserCreate
        :raises UserAlreadyRegisteredError: If a user with the same email
        already exists.
        :returns: The created user.
        :rtype: User
        """
        try:
            return await super().create(object)
        except IntegrityError:
            raise UserAlreadyRegisteredError()


class UserRepository(BaseRepository[User, UserCreate, UserUpdate]):
    """Repository for users."""

    pass
