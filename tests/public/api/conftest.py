from typing import Any, Unpack
from unittest.mock import Mock

import pytest
from fastapi_cache import FastAPICache
from pytest_mock import MockerFixture

from app.domain.entities.auth import JWTToken, JWTUser
from app.public.api.permission import create_token
from tests.factories.api.permission import JWTUserFactory


@pytest.fixture(scope='session')
def jwt_user() -> JWTUser:
    return JWTUserFactory.build()


@pytest.fixture(scope='session')
def jwt_token(jwt_user: JWTUser) -> JWTToken:
    return JWTToken(
        access_token=create_token(jwt_user),
        refresh_token=create_token(jwt_user, is_refreshed=True),
    )


@pytest.fixture(autouse=True)
def mock_jwt_decode(mocker: MockerFixture) -> None:
    return mocker.patch(
        'app.public.api.permission.decode_token',
        new_callable=Mock,
    )


class NoOpBackend:
    async def get(self, key: Any) -> None:
        return None

    async def set(self, key: Any, value: Any, expire: Any) -> None:
        return None

    async def delete(self, key: Any) -> None:
        return None

    async def get_with_ttl(*args: Unpack[Any]) -> tuple[None, None]:
        return None, None


@pytest.fixture(autouse=True)
def disable_fastapi_cache() -> None:
    FastAPICache.init(NoOpBackend())
