from typing import Any, Sequence, Type, TypeVar

from fastapi.testclient import TestClient
from pydantic import BaseModel
from pytest_mock import MockerFixture

from app.domain.entities.auth import JWTUser
from app.infrastructure.database.models.user import User

TestEntities = TypeVar('TestEntities', bound=BaseModel)
TestQuery = TypeVar('TestQuery', bound=BaseModel)


async def get_entities(
    http_client: TestClient,
    url: str,
    entities: Sequence[Type[TestEntities]],
    query: Type[TestQuery],
    sql_execute: MockerFixture,
    read_schema: Type[BaseModel],
) -> None:
    params = query.model_dump(exclude_none=True)
    entities_assert = [
        read_schema.model_validate(entity).model_dump(mode='json')
        for entity in entities
    ]

    sql_execute(scalars_all=entities)

    response = http_client.get(url, params=params)

    assert response.status_code == 200
    assert response.json() == entities_assert


async def get_entity_by_id(
    http_client: TestClient,
    url: str,
    entity: Type[TestEntities],
    sql_execute: MockerFixture,
    read_schema: Type[BaseModel],
) -> None:
    entity_assert = read_schema.model_validate(entity).model_dump(mode='json')

    sql_execute(scalars_one_or_none=entity)

    response = http_client.get(f'{url}{entity.id}')

    assert response.status_code == 200
    assert response.json() == entity_assert


async def create_entity(
    http_client: TestClient,
    url: str,
    entity: Type[TestEntities],
    entity_register: dict[str, Any],
    sql_execute: MockerFixture,
    user: User,
    jwt_decode: MockerFixture,
    read_schema: Type[BaseModel],
) -> None:
    check_user = JWTUser.model_validate(user)

    entity.user_id = user.id
    category_assert = read_schema.model_validate(entity).model_dump(
        mode='json'
    )

    sql_execute(scalar=entity)
    jwt_decode.return_value(check_user)

    response = http_client.post(url, json=entity_register)

    assert response.status_code == 201
    assert response.json() == category_assert


async def update_entity(
    http_client: TestClient,
    url: str,
    entity: Type[TestEntities],
    sql_execute: MockerFixture,
    user: User,
    jwt_decode: MockerFixture,
    read_schema: Type[BaseModel],
    update_schema: Type[BaseModel],
) -> None:
    updated_name = f'{entity.name}_test_update'
    check_user = JWTUser.model_validate(user)

    entity_update = update_schema(
        name=updated_name,
    ).model_dump()

    entity.user_id = user.id
    entity.name = updated_name

    category_assert = read_schema.model_validate(entity).model_dump(
        mode='json'
    )

    sql_execute(scalar=entity)
    jwt_decode.return_value(check_user)

    response = http_client.put(f'{url}{entity.id}', json=entity_update)

    assert response.status_code == 200
    assert response.json() == category_assert


async def delete_entity(
    http_client: TestClient,
    url: str,
    entity: Type[TestEntities],
    sql_execute: MockerFixture,
) -> None:
    sql_execute()

    response = http_client.delete(f'{url}{entity.id}')

    assert response.status_code == 204
