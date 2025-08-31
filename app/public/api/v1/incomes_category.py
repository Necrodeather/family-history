from typing import Annotated
from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Path, Query, status
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

incomes_category_router = APIRouter(prefix='/incomes_category')


@incomes_category_router.get(
    '/',
    response_description='List of incomes categories that match the query',
)
@cache(expire=60)
@inject
async def get(
    query: Annotated[CategoryQuery, Query()],
    income_category_service: Annotated[
        CategoryService,
        Depends(Provide[AppContainer.incomes_category.service]),
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> list[CategoryRead]:
    """
    Get a list of incomes categories.
    """
    return await income_category_service.get_multi(query)


@incomes_category_router.get(
    '/{category_id}',
    response_description='Retrieved incomes category',
    responses={
        404: {'model': ErrorMessage},
    },
)
@cache(expire=60)
@inject
async def get_by_id(
    category_id: Annotated[
        UUID,
        Path(
            description='Unique identifier of the incomes category \
                to retrieve.'
        ),
    ],
    income_category_service: Annotated[
        CategoryService,
        Depends(Provide[AppContainer.incomes_category.service]),
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> CategoryRead:
    """
    Get an incomes category by its ID.
    """
    return await income_category_service.get_by_id(category_id)


@incomes_category_router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    response_description='Created incomes category',
    responses={
        409: {'model': ErrorMessage},
    },
)
@inject
async def create(
    category: CategoryCreate,
    income_category_service: Annotated[
        CategoryService,
        Depends(Provide[AppContainer.incomes_category.service]),
    ],
    user: Annotated[JWTUser, Depends(decode_token)],
) -> CategoryRead:
    """
    Create a new incomes category.

    `category`: Details of the incomes category to create.
    """
    category.user_id = user.id
    return await income_category_service.create(category)


@incomes_category_router.put(
    '/{category_id}',
    response_description='Updated incomes category',
    responses={
        404: {'model': ErrorMessage},
    },
)
@inject
async def update(
    category_id: Annotated[
        UUID,
        Path(
            description='Unique identifier of the incomes category to update.'
        ),
    ],
    category: CategoryUpdate,
    income_category_service: Annotated[
        CategoryService,
        Depends(Provide[AppContainer.incomes_category.service]),
    ],
    user: Annotated[JWTUser, Depends(decode_token)],
) -> CategoryRead:
    """
    Update an incomes category by its ID.

    `category`: Details of the incomes category to update.
    """
    category.updated_user_id = user.id
    return await income_category_service.update_by_id(category_id, category)


@incomes_category_router.delete(
    '/{category_id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
@inject
async def delete(
    category_id: Annotated[
        UUID,
        Path(
            description='Unique identifier of the incomes category to delete.'
        ),
    ],
    income_category_service: Annotated[
        CategoryService,
        Depends(Provide[AppContainer.incomes_category.service]),
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> None:
    """
    Delete an incomes category by its ID.
    """
    await income_category_service.delete_by_id(category_id)
