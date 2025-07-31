from typing import Annotated
from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Query, status
from fastapi_cache.decorator import cache

from containers.root import AppContainer
from domain.entities.auth import JWTUser
from domain.entities.category import (
    CategoryCreate,
    CategoryRead,
    CategoryUpdate,
)
from domain.entities.queries import CategoryQuery
from public.api.permission import decode_token
from public.api.schemas import ErrorMessage
from services.category import CategoryService

expenses_category_router = APIRouter(prefix='/expenses_category')


@expenses_category_router.get('/')
@cache(expire=60)
@inject
async def get(
    query: Annotated[CategoryQuery, Query()],
    expenses_category_service: Annotated[
        CategoryService,
        Depends(Provide[AppContainer.expenses_category.service]),
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> list[CategoryRead]:
    return await expenses_category_service.get_multi(query)


@expenses_category_router.get(
    '/{category_id}',
    responses={
        404: {'model': ErrorMessage},
    },
)
@cache(expire=60)
@inject
async def get_by_id(
    category_id: UUID,
    expenses_category_service: Annotated[
        CategoryService,
        Depends(Provide[AppContainer.expenses_category.service]),
    ],
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
@inject
async def create(
    category: CategoryCreate,
    expenses_category_service: Annotated[
        CategoryService,
        Depends(Provide[AppContainer.expenses_category.service]),
    ],
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
@inject
async def update(
    category_id: UUID,
    category: CategoryUpdate,
    expenses_category_service: Annotated[
        CategoryService,
        Depends(Provide[AppContainer.expenses_category.service]),
    ],
    user: Annotated[JWTUser, Depends(decode_token)],
) -> CategoryRead:
    category.updated_user_id = user.id
    return await expenses_category_service.update_by_id(category_id, category)


@expenses_category_router.delete(
    '/{category_id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
@inject
async def delete(
    category_id: UUID,
    expenses_category_service: Annotated[
        CategoryService,
        Depends(Provide[AppContainer.expenses_category.service]),
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> None:
    await expenses_category_service.delete_by_id(category_id)
