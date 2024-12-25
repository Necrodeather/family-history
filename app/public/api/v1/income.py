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
from app.public.api.schemas import Message
from app.service.budget import income_service

income_router = APIRouter(prefix='/income')


@income_router.get('/')
async def get_all(
    _: Annotated[JWTUser, Depends(decode_token)],
) -> list[BudgetRead]:
    return await income_service.get_all()


@income_router.get(
    '/{category_id}',
    responses={
        404: {'model': Message},
    },
)
async def get_by_id(
    category_id: UUID,
    _: Annotated[JWTUser, Depends(decode_token)],
) -> BudgetRead:
    return await income_service.get_by_id(category_id)


@income_router.post('/', status_code=status.HTTP_201_CREATED)
async def create(
    category: BudgetCreateForm,
    _: Annotated[JWTUser, Depends(decode_token)],
) -> BudgetRead:
    return await income_service.create(category)


@income_router.put(
    '/{category_id}',
    responses={
        404: {'model': Message},
    },
)
async def update(
    category_id: UUID,
    category: BudgetUpdateForm,
    _: Annotated[JWTUser, Depends(decode_token)],
) -> BudgetRead:
    return await income_service.update_by_id(category_id, category)


@income_router.delete('/{category_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    category_id: UUID,
    _: Annotated[JWTUser, Depends(decode_token)],
) -> None:
    await income_service.delete_by_id(category_id)
