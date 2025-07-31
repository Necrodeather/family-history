from typing import Annotated
from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Query, status
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

expenses_router = APIRouter(prefix='/expenses')


@expenses_router.get('/')
@cache(expire=60)
@inject
async def get(
    query: Annotated[BudgetQuery, Query()],
    expenses_service: Annotated[
        BudgetService,
        Depends(Provide[AppContainer.expenses.service]),
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> list[BudgetRead]:
    return await expenses_service.get_multi(query)


@expenses_router.get(
    '/{expenses_id}',
    responses={
        404: {'model': ErrorMessage},
    },
)
@cache(expire=60)
@inject
async def get_by_id(
    expenses_id: UUID,
    expenses_service: Annotated[
        BudgetService,
        Depends(Provide[AppContainer.expenses.service]),
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> BudgetRead:
    return await expenses_service.get_by_id(expenses_id)


@expenses_router.post('/', status_code=status.HTTP_201_CREATED)
@inject
async def create(
    expenses: BudgetCreate,
    expenses_service: Annotated[
        BudgetService,
        Depends(Provide[AppContainer.expenses.service]),
    ],
    user: Annotated[JWTUser, Depends(decode_token)],
) -> BudgetRead:
    expenses.user_id = user.id
    return await expenses_service.create(expenses)


@expenses_router.put(
    '/{expenses_id}',
    responses={
        404: {'model': ErrorMessage},
    },
)
@inject
async def update(
    expenses_id: UUID,
    expenses: BudgetUpdate,
    expenses_service: Annotated[
        BudgetService,
        Depends(Provide[AppContainer.expenses.service]),
    ],
    user: Annotated[JWTUser, Depends(decode_token)],
) -> BudgetRead:
    expenses.updated_user_id = user.id
    return await expenses_service.update_by_id(expenses_id, expenses)


@expenses_router.delete(
    '/{expenses_id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
@inject
async def delete(
    expenses_id: UUID,
    expenses_service: Annotated[
        BudgetService,
        Depends(Provide[AppContainer.expenses.service]),
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> None:
    await expenses_service.delete_by_id(expenses_id)
