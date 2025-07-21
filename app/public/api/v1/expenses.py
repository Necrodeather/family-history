from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, status

from app.domain.entities.auth import JWTUser
from app.domain.entities.budget import (
    BudgetCreateForm,
    BudgetRead,
    BudgetUpdateForm,
)
from app.public.api.permission import decode_token
from app.public.api.schemas import BudgetQueryApi, ErrorMessage
from app.service.budget import expenses_service

expenses_router = APIRouter(prefix='/expenses')


@expenses_router.get('/')
async def get(
    query: Annotated[BudgetQueryApi, Depends()],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> list[BudgetRead]:
    return await expenses_service.get_multi(query)


@expenses_router.get(
    '/{expenses_id}',
    responses={
        404: {'model': ErrorMessage},
    },
)
async def get_by_id(
    expenses_id: UUID,
    _: Annotated[JWTUser, Depends(decode_token)],
) -> BudgetRead:
    return await expenses_service.get_by_id(expenses_id)


@expenses_router.post('/', status_code=status.HTTP_201_CREATED)
async def create(
    expenses: BudgetCreateForm,
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
async def update(
    expenses_id: UUID,
    expenses: BudgetUpdateForm,
    user: Annotated[JWTUser, Depends(decode_token)],
) -> BudgetRead:
    expenses.updated_user_id = user.id
    return await expenses_service.update_by_id(expenses_id, expenses)


@expenses_router.delete(
    '/{expenses_id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    expenses_id: UUID,
    _: Annotated[JWTUser, Depends(decode_token)],
) -> None:
    await expenses_service.delete_by_id(expenses_id)
