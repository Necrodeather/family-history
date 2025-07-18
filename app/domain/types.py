from typing import TypeVar

from pydantic import BaseModel

from app.infrastructure.database.base import Base

ModelType = TypeVar('ModelType', bound=Base)
QuerySchemaType = TypeVar('QuerySchemaType', bound=BaseModel)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)
ReadSchemaType = TypeVar('ReadSchemaType', bound=BaseModel)
