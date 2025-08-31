from datetime import date, datetime
from decimal import Decimal
from typing import Annotated
from uuid import UUID, uuid4

from sqlalchemy import DECIMAL, Date, DateTime, MetaData, String
from sqlalchemy.orm import DeclarativeBase, mapped_column, registry
from sqlalchemy_utils import EmailType, PasswordType, UUIDType

uuid_pk = Annotated[
    UUID,
    mapped_column(
        UUIDType(binary=False),
        primary_key=True,
        default=uuid4,
    ),
]

uuid = Annotated[UUID, False]
decimal = Annotated[Decimal, (10, 2)]
str_64 = Annotated[str, 64]
str_128 = Annotated[str, 128]
password = Annotated[bytes, PasswordType]
email_sql = Annotated[str, EmailType]
date_sql = date
datetime_timezone = Annotated[datetime, True]

meta = MetaData(
    schema='family_history',
    naming_convention={
        'ix': 'ix_%(column_0_label)s',
        'uq': 'uq_%(table_name)s_%(column_0_name)s',
        'ck': 'ck_%(table_name)s_%(constraint_name)s',
        'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
        'pk': 'pk_%(table_name)s',
    },
)


class Base(DeclarativeBase):
    """Base class for all database models."""
    metadata = meta

    registry = registry(
        type_annotation_map={
            str_64: String(64),
            str_128: String(128),
            datetime_timezone: DateTime(timezone=True),
            date_sql: Date(),
            password: PasswordType(schemes=['bcrypt']),
            email_sql: EmailType(),
            decimal: DECIMAL(10, 2),
        },
    )
