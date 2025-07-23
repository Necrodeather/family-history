from typing import AsyncIterator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.domain.entities.auth import JWTToken
from app.public.api.app import create_app
from app.public.api.schemas import (
    BudgetQueryApi,
    CategoryQueryApi,
    UserQueryApi,
)
from tests.factories.api.queries import (
    BudgetQueryApiFactory,
    CategoryQueryApiFactory,
    UserQueryApiFactory,
)


@pytest.fixture(scope='session')
def fastapi_app() -> FastAPI:
    return create_app()


@pytest.fixture(scope='session')
async def http_client(
    fastapi_app: FastAPI,
) -> AsyncIterator[TestClient]:
    yield TestClient(
        app=fastapi_app,
        base_url='http://test',
    )


@pytest.fixture(scope='session')
async def authenticated_http_client(
    fastapi_app: FastAPI,
    jwt_token: JWTToken,
) -> AsyncIterator[TestClient]:
    yield TestClient(
        app=fastapi_app,
        base_url='http://test',
        headers={'Authorization': f'Bearer {jwt_token.access_token.payload}'},
    )


@pytest.fixture(scope='session')
def user_query() -> UserQueryApi:
    return UserQueryApiFactory.build()


@pytest.fixture(scope='session')
def category_query() -> CategoryQueryApi:
    return CategoryQueryApiFactory.build()

@pytest.fixture(scope='session')
def budget_query() -> BudgetQueryApi:
    return BudgetQueryApiFactory.build()
