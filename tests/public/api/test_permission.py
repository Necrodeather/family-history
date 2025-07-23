import pytest
from pytest_mock import MockerFixture

from app.domain.entities.auth import JWTToken, JWTUser
from app.domain.exceptions import CredentialsError
from app.public.api.permission import create_token, decode_token

pytestmark = pytest.mark.asyncio


async def test_decode_token(jwt_token: JWTToken, jwt_user: JWTUser) -> None:
    assert await decode_token(jwt_token.access_token.payload) == jwt_user


async def test_decode_token_error(
    jwt_user: JWTUser,
    mocker: MockerFixture,
) -> None:
    token = create_token(jwt_user)
    with pytest.raises(CredentialsError):
        await decode_token('test_error_token')

    mocker.patch('app.public.api.permission.decode').return_value = {}

    with pytest.raises(CredentialsError):
        await decode_token(token.payload)
