from typing import Annotated

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from containers.root import AppContainer
from domain.entities.auth import JWTToken, JWTUser, LoginUser
from domain.entities.user import UserCreate, UserRead
from public.api.permission import (
    create_token,
    decode_token,
)
from public.api.schemas import ErrorMessage
from service.user import AuthService

auth_router = APIRouter(prefix='/auth')


@auth_router.post(
    '/login',
    responses={
        401: {'model': ErrorMessage},
    },
)
@inject
async def login(
    login_user_form: LoginUser,
    auth_service: Annotated[
        AuthService,
        Depends(Provide[AppContainer.auth.service]),
    ],
) -> JWTToken:
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
@inject
async def register(
    create_user_form: UserCreate,
    auth_service: Annotated[
        AuthService,
        Depends(Provide[AppContainer.auth.service]),
    ],
) -> UserRead:
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
@inject
async def me(
    auth_service: Annotated[
        AuthService,
        Depends(Provide[AppContainer.auth.service]),
    ],
    user: Annotated[JWTUser, Depends(decode_token)],
) -> UserRead:
    return await auth_service.get_by_id(user.id)
