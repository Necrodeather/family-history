from app.domain.entities.auth import LoginUser
from app.domain.entities.user import UserCreate, UserRead, UserUpdate
from app.domain.exceptions import IncorrectLoginError
from app.infrastructure.database.repository.crud.user import (
    auth_crud,
    user_crud,
)
from app.infrastructure.database.uow import SqlAlchemyUnitOfWork
from app.service.base import AppCRUDService


class AuthService(
    AppCRUDService[
        UserCreate,
        UserUpdate,
        UserRead,
    ]
):
    async def login(self, login_data: LoginUser) -> UserRead:
        async with self._uow as uow:
            user = await uow.repository.get_user_by_email(login_data.email)  # type: ignore[attr-defined]
        if not user or not login_data.password == user.password:
            raise IncorrectLoginError()
        return UserRead.model_validate(user)


class UserService(
    AppCRUDService[
        UserCreate,
        UserUpdate,
        UserRead,
    ]
):
    pass


auth_service = AuthService(
    SqlAlchemyUnitOfWork(auth_crud),
    UserRead,
)
user_service = UserService(
    SqlAlchemyUnitOfWork(user_crud),
    UserRead,
)
