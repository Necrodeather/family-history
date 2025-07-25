from typing import Annotated
from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Query, status

from app.core.depends import ApiContainer
from app.domain.entities.auth import JWTUser
from app.domain.entities.category import (
    CategoryCreate,
    CategoryRead,
    CategoryUpdate,
)
from app.domain.entities.queries import CategoryQuery
from app.public.api.permission import decode_token
from app.public.api.schemas import ErrorMessage
from app.service.category import CategoryService

incomes_category_router = APIRouter(prefix='/incomes_category')


@incomes_category_router.get('/')
@inject
async def get(
    query: Annotated[CategoryQuery, Query()],
    income_category_service: Annotated[
        CategoryService,
        Depends(Provide[ApiContainer.income_category_service]),
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> list[CategoryRead]:
    return await income_category_service.get_multi(query)


@incomes_category_router.get(
    '/{category_id}',
    responses={
        404: {'model': ErrorMessage},
    },
)
@inject
async def get_by_id(
    category_id: UUID,
    income_category_service: Annotated[
        CategoryService,
        Depends(Provide[ApiContainer.income_category_service]),
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> CategoryRead:
    return await income_category_service.get_by_id(category_id)


@incomes_category_router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    responses={
        409: {'model': ErrorMessage},
    },
)
@inject
async def create(
    category: CategoryCreate,
    income_category_service: Annotated[
        CategoryService,
        Depends(Provide[ApiContainer.income_category_service]),
    ],
    user: Annotated[JWTUser, Depends(decode_token)],
) -> CategoryRead:
    category.user_id = user.id
    return await income_category_service.create(category)


@incomes_category_router.put(
    '/{category_id}',
    responses={
        404: {'model': ErrorMessage},
    },
)
@inject
async def update(
    category_id: UUID,
    category: CategoryUpdate,
    income_category_service: Annotated[
        CategoryService,
        Depends(Provide[ApiContainer.income_category_service]),
    ],
    user: Annotated[JWTUser, Depends(decode_token)],
) -> CategoryRead:
    category.updated_user_id = user.id
    return await income_category_service.update_by_id(category_id, category)


@incomes_category_router.delete(
    '/{category_id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
@inject
async def delete(
    category_id: UUID,
    income_category_service: Annotated[
        CategoryService,
        Depends(Provide[ApiContainer.income_category_service]),
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> None:
    await income_category_service.delete_by_id(category_id)
