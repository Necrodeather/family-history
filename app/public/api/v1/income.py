from typing import Annotated
from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Path, Query, status
from fastapi_cache.decorator import cache

from containers.root import AppContainer
from domain.entities.auth import JWTUser
from domain.entities.budget import (
    BudgetCreate,
    BudgetRead,
    BudgetUpdate,
)
from domain.entities.queries import BudgetQuery
from public.api.permission import decode_token
from public.api.schemas import ErrorMessage
from services.budget import BudgetService

income_router = APIRouter(prefix='/income')


@income_router.get(
    '/',
    response_description='List of incomes that match the query',
)
@cache(expire=60)
@inject
async def get(
    query: Annotated[BudgetQuery, Query()],
    income_service: Annotated[
        BudgetService,
        Depends(Provide[AppContainer.income.service]),
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> list[BudgetRead]:
    """
    Get a list of incomes.
    """
    return await income_service.get_multi(query)


@income_router.get(
    '/{income_id}',
    response_description='Retrieved income',
    responses={
        404: {'model': ErrorMessage},
    },
)
@cache(expire=60)
@inject
async def get_by_id(
    income_id: Annotated[
        UUID,
        Path(description='Unique identifier of the income to retrieve.'),
    ],
    income_service: Annotated[
        BudgetService,
        Depends(Provide[AppContainer.income.service]),
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> BudgetRead:
    """
    Get an income by its ID.
    """
    return await income_service.get_by_id(income_id)


@income_router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    response_description='Created income',
    responses={
        409: {'model': ErrorMessage},
    },
)
@inject
async def create(
    income: BudgetCreate,
    income_service: Annotated[
        BudgetService,
        Depends(Provide[AppContainer.income.service]),
    ],
    user: Annotated[JWTUser, Depends(decode_token)],
) -> BudgetRead:
    """
    Create a new income.

    `income`: Details of the income to create.
    """
    income.user_id = user.id
    return await income_service.create(income)


@income_router.put(
    '/{income_id}',
    response_description='Updated income',
    responses={
        404: {'model': ErrorMessage},
    },
)
@inject
async def update(
    income_id: Annotated[
        UUID,
        Path(description='Unique identifier of the income to update.'),
    ],
    income: BudgetUpdate,
    income_service: Annotated[
        BudgetService,
        Depends(Provide[AppContainer.income.service]),
    ],
    user: Annotated[JWTUser, Depends(decode_token)],
) -> BudgetRead:
    """
    Update an income by its ID.

    `income`: Details of the income to update.
    """
    income.updated_user_id = user.id
    return await income_service.update_by_id(income_id, income)


@income_router.delete(
    '/{income_id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
@inject
async def delete(
    income_id: Annotated[
        UUID,
        Path(description='Unique identifier of the income to delete.'),
    ],
    income_service: Annotated[
        BudgetService,
        Depends(Provide[AppContainer.income.service]),
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> None:
    """
    Delete an income by its ID.
    """
    await income_service.delete_by_id(income_id)
