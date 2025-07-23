import pytest
from fastapi.testclient import TestClient
from pytest_mock import MockerFixture

from app.domain.entities.auth import JWTToken, JWTUser, LoginUser, Token
from app.domain.entities.user import UserCreate, UserRead
from app.infrastructure.database.models.user import User

pytestmark = pytest.mark.asyncio


@pytest.fixture
def endpoint_url() -> str:
    return '/api/v1/auth'


async def test_login(
    http_client: TestClient,
    endpoint_url: str,
    user: User,
    mock_execute: MockerFixture,
    mocker: MockerFixture,
    jwt_token: JWTToken,
) -> None:
    user_login = LoginUser(
        email=user.email,
        password=user.password.test_password,
    ).model_dump()

    mock_execute(scalar=user)
    mocker.patch(
        'app.public.api.v1.auth.create_token',
        side_effect=[
            Token(
                payload=jwt_token.access_token.payload,
                expire=jwt_token.access_token.expire,
            ),
            Token(
                payload=jwt_token.refresh_token.payload,
                expire=jwt_token.refresh_token.expire,
            ),
        ],
    )

    response = http_client.post(
        f'{endpoint_url}/login',
        json=user_login,
    )

    assert response.status_code == 200
    assert response.json() == jwt_token.model_dump()


async def test_register(
    http_client: TestClient,
    endpoint_url: str,
    user: User,
    mock_execute: MockerFixture,
) -> None:
    mock_execute(scalar=user)

    user_assert = UserRead.model_validate(user).model_dump(mode='json')
    user_register = UserCreate(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=user.password.test_password,
    ).model_dump()

    response = http_client.post(
        f'{endpoint_url}/register',
        json=user_register,
    )

    assert response.status_code == 201
    assert response.json() == user_assert


async def test_refresh_access_token(
    authenticated_http_client: TestClient,
    endpoint_url: str,
    user: User,
    jwt_token: JWTToken,
    mocker: MockerFixture,
    mock_jwt_decode: MockerFixture,
) -> None:
    check_user = JWTUser.model_validate(user)

    mock_jwt_decode.return_value(check_user)
    mocker.patch(
        'app.public.api.v1.auth.create_token',
        side_effect=[
            Token(
                payload=jwt_token.access_token.payload,
                expire=jwt_token.access_token.expire,
            ),
            Token(
                payload=jwt_token.refresh_token.payload,
                expire=jwt_token.refresh_token.expire,
            ),
        ],
    )

    response = authenticated_http_client.post(f'{endpoint_url}/refresh')

    assert response.status_code == 200
    assert response.json() == jwt_token.model_dump()


async def test_me(
    authenticated_http_client: TestClient,
    endpoint_url: str,
    user: User,
    mock_execute: MockerFixture,
    mock_jwt_decode: MockerFixture,
) -> None:
    user_assert = UserRead.model_validate(user).model_dump(mode='json')
    check_user = JWTUser.model_validate(user)

    mock_execute(scalars_one_or_none=user)
    mock_jwt_decode.return_value(check_user)

    response = authenticated_http_client.get(f'{endpoint_url}/me')

    assert response.status_code == 200
    assert response.json() == user_assert
