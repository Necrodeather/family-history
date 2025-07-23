from typing import Sequence

import pytest
from fastapi.testclient import TestClient
from pytest_mock import MockerFixture

from app.domain.entities.user import UserRead
from app.infrastructure.database.models.user import User
from app.public.api.schemas import UserQueryApi

pytestmark = pytest.mark.asyncio


@pytest.fixture
def endpoint_url() -> str:
    return '/api/v1/user/'


async def test_get_users(
    authenticated_http_client: TestClient,
    endpoint_url: str,
    users: Sequence[User],
    user_query: UserQueryApi,
    mock_execute: MockerFixture,
) -> None:
    params = user_query.model_dump(exclude_none=True)
    user_assert = [
        UserRead.model_validate(user).model_dump(mode="json") for user in users
    ]

    mock_execute(scalars_all=users)

    response = authenticated_http_client.get(endpoint_url, params=params)

    assert response.status_code == 200
    assert response.json() == user_assert


async def test_get_user_by_id(
    authenticated_http_client: TestClient,
    endpoint_url: str,
    user: User,
    mock_execute: MockerFixture,
) -> None:
    user_assert = UserRead.model_validate(user).model_dump(mode="json")

    mock_execute(scalars_one_or_none=user)

    response = authenticated_http_client.get(f'{endpoint_url}{user.id}')

    assert response.status_code == 200
    assert response.json() == user_assert
