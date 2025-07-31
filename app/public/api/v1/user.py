from typing import Annotated
from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Query
from fastapi_cache.decorator import cache

from containers.root import AppContainer
from domain.entities.auth import JWTUser
from domain.entities.queries import UserQuery
from domain.entities.user import UserRead
from public.api.permission import decode_token
from public.api.schemas import ErrorMessage
from services.user import UserService

user_router = APIRouter(prefix='/user')


@user_router.get('/')
@cache(expire=60)
@inject
async def get(
    query: Annotated[UserQuery, Query()],
    user_service: Annotated[
        UserService, Depends(Provide[AppContainer.user.service])
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> list[UserRead]:
    return await user_service.get_multi(query)


@user_router.get(
    '/{user_id}',
    responses={
        404: {'model': ErrorMessage},
    },
)
@cache(expire=60)
@inject
async def get_by_id(
    user_id: UUID,
    user_service: Annotated[
        UserService, Depends(Provide[AppContainer.user.service])
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> UserRead:
    return await user_service.get_by_id(user_id)
