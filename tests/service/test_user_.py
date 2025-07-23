import pytest
from pytest_mock import MockerFixture

from app.domain.entities.auth import LoginUser
from app.domain.entities.user import UserCreate
from app.domain.exceptions import (
    IncorrectLoginError,
    UserAlreadyRegisteredError,
)
from app.infrastructure.database.models.user import User
from app.service.user import auth_service

pytestmark = pytest.mark.asyncio


async def test_auth_service_create_error(
    user: User,
    mock_execute: MockerFixture,
) -> None:
    mock_execute(raise_error=True)
    user_create = UserCreate(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=user.password.test_password,
    )
    with pytest.raises(UserAlreadyRegisteredError):
        await auth_service.create(user_create)


async def test_auth_service_login_error(
    user: User,
    mock_execute: MockerFixture,
) -> None:
    mock_execute(scalar=user)
    user_create = LoginUser(
        email=user.email,
        password='test',
    )
    with pytest.raises(IncorrectLoginError):
        await auth_service.login(user_create)
