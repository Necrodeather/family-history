from uuid import UUID

from fastapi import APIRouter

from app.domain.entities.category import CategoryCreateUpdateForm, CategoryRead
from app.service.category import expenses_category_service

expenses_category_router = APIRouter(prefix='/category')


@expenses_category_router.get('/')
async def get_all() -> list[CategoryRead]:
    return await expenses_category_service.get_all()


@expenses_category_router.get('/{category_id}')
async def get_by_id(category_id: UUID) -> CategoryRead:
    return await expenses_category_service.get_by_id(category_id)


@expenses_category_router.post('/')
async def create(
    category: CategoryCreateUpdateForm,
) -> CategoryRead:
    return await expenses_category_service.create(category)


@expenses_category_router.put('/{category_id}')
async def update(
    category_id: UUID,
    category: CategoryCreateUpdateForm,
) -> CategoryRead:
    return await expenses_category_service.update_by_id(category_id, category)


@expenses_category_router.delete('/{category_id}')
async def delete(
    category_id: UUID,
) -> None:
    await expenses_category_service.delete_by_id(category_id)
