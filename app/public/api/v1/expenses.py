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

expenses_router = APIRouter(prefix='/expenses')


@expenses_router.get(
    '/',
    response_description='List of expenses that match the query',
)
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
    """
    Get a list of expenses.
    """
    return await expenses_service.get_multi(query)


@expenses_router.get(
    '/{budget_id}',
    response_description='Retrieved expense',
    responses={
        404: {'model': ErrorMessage},
    },
)
@cache(expire=60)
@inject
async def get_by_id(
    budget_id: Annotated[
        UUID,
        Path(description='Unique identifier of the expense to retrieve.'),
    ],
    expenses_service: Annotated[
        BudgetService,
        Depends(Provide[AppContainer.expenses.service]),
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> BudgetRead:
    """
    Get an expense by its ID.
    """
    return await expenses_service.get_by_id(budget_id)


@expenses_router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    response_description='Created expense',
    responses={
        409: {'model': ErrorMessage},
    },
)
@inject
async def create(
    budget: BudgetCreate,
    expenses_service: Annotated[
        BudgetService,
        Depends(Provide[AppContainer.expenses.service]),
    ],
    user: Annotated[JWTUser, Depends(decode_token)],
) -> BudgetRead:
    """
    Create a new expense.

    `budget`: Details of the expense to create.
    """
    budget.user_id = user.id
    return await expenses_service.create(budget)


@expenses_router.put(
    '/{budget_id}',
    response_description='Updated expense',
    responses={
        404: {'model': ErrorMessage},
    },
)
@inject
async def update(
    budget_id: Annotated[
        UUID,
        Path(description='Unique identifier of the expense to update.'),
    ],
    budget: BudgetUpdate,
    expenses_service: Annotated[
        BudgetService,
        Depends(Provide[AppContainer.expenses.service]),
    ],
    user: Annotated[JWTUser, Depends(decode_token)],
) -> BudgetRead:
    """
    Update an expense by its ID.

    `budget`: Details of the expense to update.
    """
    budget.updated_user_id = user.id
    return await expenses_service.update_by_id(budget_id, budget)


@expenses_router.delete(
    '/{budget_id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
@inject
async def delete(
    budget_id: Annotated[
        UUID,
        Path(description='Unique identifier of the expense to delete.'),
    ],
    expenses_service: Annotated[
        BudgetService,
        Depends(Provide[AppContainer.expenses.service]),
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> None:
    """
    Delete an expense by its ID.
    """
    await expenses_service.delete_by_id(budget_id)
