from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.domain.entities.auth import JWTToken, JWTUser, LoginUser
from app.domain.entities.user import UserCreate, UserRead
from app.public.api.permission import (
    create_token,
    decode_token,
)
from app.public.api.schemas import ErrorMessage
from app.service.user import auth_service

auth_router = APIRouter(prefix='/auth')


@auth_router.post(
    '/login',
    responses={
        401: {'model': ErrorMessage},
    },
)
async def login(login_user_form: LoginUser) -> JWTToken:
    user = await auth_service.login(login_user_form)
    jwt_user = JWTUser.model_validate(user)
    return JWTToken(
        access_token=create_token(jwt_user),
        refresh_token=create_token(jwt_user, is_refreshed=True),
    )


@auth_router.post(
    '/register',
    status_code=status.HTTP_201_CREATED,
    responses={
        409: {'model': ErrorMessage},
    },
)
async def register(create_user_form: UserCreate) -> UserRead:
    return await auth_service.create(create_user_form)


@auth_router.post('/refresh')
async def refresh_access_token(
    jwt_user: Annotated[JWTUser, Depends(decode_token)],
) -> JWTToken:
    return JWTToken(
        access_token=create_token(jwt_user),
        refresh_token=create_token(jwt_user, is_refreshed=True),
    )


@auth_router.get('/me')
async def me(
    user: Annotated[JWTUser, Depends(decode_token)],
) -> UserRead:
    return await auth_service.get_by_id(user.id)
