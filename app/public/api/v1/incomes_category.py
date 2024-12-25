from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, status

from app.domain.entities.auth import JWTUser
from app.domain.entities.category import CategoryCreateUpdateForm, CategoryRead
from app.public.api.permission import decode_token
from app.public.api.schemas import Message
from app.service.category import income_category_service

incomes_category_router = APIRouter(prefix='/incomes_category')


@incomes_category_router.get('/')
async def get_all(
    _: Annotated[JWTUser, Depends(decode_token)],
) -> list[CategoryRead]:
    return await income_category_service.get_all()


@incomes_category_router.get(
    '/{category_id}',
    responses={
        404: {'model': Message},
    },
)
async def get_by_id(
    category_id: UUID,
    _: Annotated[JWTUser, Depends(decode_token)],
) -> CategoryRead:
    return await income_category_service.get_by_id(category_id)


@incomes_category_router.post('/', status_code=status.HTTP_201_CREATED)
async def create(
    category: CategoryCreateUpdateForm,
    _: Annotated[JWTUser, Depends(decode_token)],
) -> CategoryRead:
    return await income_category_service.create(category)


@incomes_category_router.put(
    '/{category_id}',
    responses={
        404: {'model': Message},
    },
)
async def update(
    category_id: UUID,
    category: CategoryCreateUpdateForm,
    _: Annotated[JWTUser, Depends(decode_token)],
) -> CategoryRead:
    return await income_category_service.update_by_id(category_id, category)


@incomes_category_router.delete(
    '/{category_id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    category_id: UUID,
    _: Annotated[JWTUser, Depends(decode_token)],
) -> None:
    await income_category_service.delete_by_id(category_id)
