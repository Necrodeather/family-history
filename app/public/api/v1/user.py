from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache

from app.domain.entities.auth import JWTUser
from app.domain.entities.user import UserRead
from app.public.api.permission import decode_token
from app.public.api.schemas import ErrorMessage, UserQueryApi
from app.service.user import user_service

user_router = APIRouter(prefix='/user')


@user_router.get('/')
@cache(expire=60)
async def get(
    query: Annotated[UserQueryApi, Depends()],
    _: Annotated[JWTUser, Depends(decode_token)],
) -> list[UserRead]:
    return await user_service.get_multi(query)


@user_router.get(
    '/{user_id}',
    responses={
        404: {'model': ErrorMessage},
    },
)
async def get_by_id(
    user_id: UUID,
    _: Annotated[JWTUser, Depends(decode_token)],
) -> UserRead:
    return await user_service.get_by_id(user_id)
