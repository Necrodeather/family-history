from typing import Annotated
from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Path, Query
from fastapi_cache.decorator import cache

from containers.root import AppContainer
from domain.entities.auth import JWTUser
from domain.entities.queries import UserQuery
from domain.entities.user import UserRead
from public.api.permission import decode_token
from public.api.schemas import ErrorMessage
from services.user import UserService

user_router = APIRouter(prefix='/user')


@user_router.get(
    '/',
    response_description='List of users that match the query',
)
@cache(expire=60)
@inject
async def get(
    query: Annotated[UserQuery, Query()],
    user_service: Annotated[
        UserService, Depends(Provide[AppContainer.user.service])
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> list[UserRead]:
    """
    Get a list of users.
    """
    return await user_service.get_multi(query)


@user_router.get(
    '/{user_id}',
    response_description='Retrieved user',
    responses={
        404: {'model': ErrorMessage},
    },
)
@cache(expire=60)
@inject
async def get_by_id(
    user_id: Annotated[
        UUID,
        Path(description='Unique identifier of the user to retrieve.'),
    ],
    user_service: Annotated[
        UserService, Depends(Provide[AppContainer.user.service])
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> UserRead:
    """
    Get a user by its ID.
    """
    return await user_service.get_by_id(user_id)
