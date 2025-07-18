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
from app.service.budget import income_service

income_router = APIRouter(prefix='/income')


@income_router.get('/')
async def get(
    query: Annotated[BudgetQueryApi, Depends()],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> list[BudgetRead]:
    return await income_service.get_multi(query)


@income_router.get(
    '/{income_id}',
    responses={
        404: {'model': ErrorMessage},
    },
)
async def get_by_id(
    income_id: UUID,
    _: Annotated[JWTUser, Depends(decode_token)],
) -> BudgetRead:
    return await income_service.get_by_id(income_id)


@income_router.post('/', status_code=status.HTTP_201_CREATED)
async def create(
    income: BudgetCreateForm,
    _: Annotated[JWTUser, Depends(decode_token)],
) -> BudgetRead:
    return await income_service.create(income)


@income_router.put(
    '/{income_id}',
    responses={
        404: {'model': ErrorMessage},
    },
)
async def update(
    income_id: UUID,
    income: BudgetUpdateForm,
    _: Annotated[JWTUser, Depends(decode_token)],
) -> BudgetRead:
    return await income_service.update_by_id(income_id, income)


@income_router.delete('/{income_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    income_id: UUID,
    _: Annotated[JWTUser, Depends(decode_token)],
) -> None:
    await income_service.delete_by_id(income_id)
