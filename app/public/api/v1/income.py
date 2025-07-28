from typing import Annotated
from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Query, status

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
from service.budget import BudgetService

income_router = APIRouter(prefix='/income')


@income_router.get('/')
@inject
async def get(
    query: Annotated[BudgetQuery, Query()],
    income_service: Annotated[
        BudgetService,
        Depends(Provide[AppContainer.income.service]),
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> list[BudgetRead]:
    return await income_service.get_multi(query)


@income_router.get(
    '/{income_id}',
    responses={
        404: {'model': ErrorMessage},
    },
)
@inject
async def get_by_id(
    income_id: UUID,
    income_service: Annotated[
        BudgetService,
        Depends(Provide[AppContainer.income.service]),
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> BudgetRead:
    return await income_service.get_by_id(income_id)


@income_router.post('/', status_code=status.HTTP_201_CREATED)
@inject
async def create(
    income: BudgetCreate,
    income_service: Annotated[
        BudgetService,
        Depends(Provide[AppContainer.income.service]),
    ],
    user: Annotated[JWTUser, Depends(decode_token)],
) -> BudgetRead:
    income.user_id = user.id
    return await income_service.create(income)


@income_router.put(
    '/{income_id}',
    responses={
        404: {'model': ErrorMessage},
    },
)
@inject
async def update(
    income_id: UUID,
    income: BudgetUpdate,
    income_service: Annotated[
        BudgetService,
        Depends(Provide[AppContainer.income.service]),
    ],
    user: Annotated[JWTUser, Depends(decode_token)],
) -> BudgetRead:
    income.updated_user_id = user.id
    return await income_service.update_by_id(income_id, income)


@income_router.delete('/{income_id}', status_code=status.HTTP_204_NO_CONTENT)
@inject
async def delete(
    income_id: UUID,
    income_service: Annotated[
        BudgetService,
        Depends(Provide[AppContainer.income.service]),
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> None:
    await income_service.delete_by_id(income_id)
