from typing import Annotated
from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Query

from app.core.depends import ApiContainer
from app.domain.entities.auth import JWTUser
from app.domain.entities.queries import UserQuery
from app.domain.entities.user import UserRead
from app.public.api.permission import decode_token
from app.public.api.schemas import ErrorMessage
from app.service.user import UserService

user_router = APIRouter(prefix='/user')


@user_router.get('/')
@inject
async def get(
    query: Annotated[UserQuery, Query()],
    user_service: Annotated[
        UserService, Depends(Provide[ApiContainer.user_service])
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
@inject
async def get_by_id(
    user_id: UUID,
    user_service: Annotated[
        UserService, Depends(Provide[ApiContainer.user_service])
    ],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> UserRead:
    return await user_service.get_by_id(user_id)
