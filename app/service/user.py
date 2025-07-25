from app.domain.entities.auth import LoginUser
from app.domain.entities.user import UserCreate, UserRead, UserUpdate
from app.domain.exceptions import IncorrectLoginError
from app.service.base import BaseService


class AuthService(
    BaseService[
        UserCreate,
        UserUpdate,
        UserRead,
    ]
):
    async def login(self, login_data: LoginUser) -> UserRead:
        user = await self._repository.get_user_by_email(login_data.email)  # type: ignore[attr-defined]
        if not user or not login_data.password == user.password:
            raise IncorrectLoginError()
        return UserRead.model_validate(user)


class UserService(
    BaseService[
        UserCreate,
        UserUpdate,
        UserRead,
    ]
):
    pass
