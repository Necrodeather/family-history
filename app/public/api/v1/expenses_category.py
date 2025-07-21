from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, status

from app.domain.entities.auth import JWTUser
from app.domain.entities.category import (
    CategoryCreateForm,
    CategoryRead,
    CategoryUpdateForm,
)
from app.public.api.permission import decode_token
from app.public.api.schemas import CategoryQueryApi, ErrorMessage
from app.service.category import expenses_category_service

expenses_category_router = APIRouter(prefix='/expenses_category')


@expenses_category_router.get('/')
async def get(
    query: Annotated[CategoryQueryApi, Depends()],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> list[CategoryRead]:
    return await expenses_category_service.get_multi(query)


@expenses_category_router.get(
    '/{category_id}',
    responses={
        404: {'model': ErrorMessage},
    },
)
async def get_by_id(
    category_id: UUID,
    _: Annotated[JWTUser, Depends(decode_token)],
) -> CategoryRead:
    return await expenses_category_service.get_by_id(category_id)


@expenses_category_router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    responses={
        409: {'model': ErrorMessage},
    },
)
async def create(
    category: CategoryCreateForm,
    user: Annotated[JWTUser, Depends(decode_token)],
) -> CategoryRead:
    category.user_id = user.id
    return await expenses_category_service.create(category)


@expenses_category_router.put(
    '/{category_id}',
    responses={
        404: {'model': ErrorMessage},
    },
)
async def update(
    category_id: UUID,
    category: CategoryUpdateForm,
    user: Annotated[JWTUser, Depends(decode_token)],
) -> CategoryRead:
    category.updated_user_id = user.id
    return await expenses_category_service.update_by_id(category_id, category)


@expenses_category_router.delete(
    '/{category_id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    category_id: UUID,
    _: Annotated[JWTUser, Depends(decode_token)],
) -> None:
    await expenses_category_service.delete_by_id(category_id)
