from uuid import uuid4, UUID

from datetime import datetime, date
from typing import Annotated
from decimal import Decimal

from sqlalchemy import DateTime, MetaData, String, Date, DECIMAL
from sqlalchemy.orm import DeclarativeBase, mapped_column, registry
from sqlalchemy_utils import EmailType, PasswordType, UUIDType, PhoneNumberType


uuid_pk = Annotated[
    UUID,
    mapped_column(UUIDType, primary_key=True, default=uuid4()),
]

decimal = Annotated[Decimal, (10, 2)]
str_64 = Annotated[str, 64]
str_128 = Annotated[str, 128]
password = Annotated[bytes, PasswordType]
email = Annotated[str, EmailType]
phone = Annotated[str, PhoneNumberType]
date_sql = date
datetime_timezone = Annotated[datetime, True]

meta = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    },
)


class Base(DeclarativeBase):
    metadata = meta

    registry = registry(
        type_annotation_map={
            str_64: String(64),
            str_128: String(128),
            datetime_timezone: DateTime(timezone=True),
            date_sql: Date(),
            password: PasswordType(schemes=["bcrypt"]),
            email: EmailType(),
            uuid_pk: UUIDType(),
            phone: PhoneNumberType(),
            decimal: DECIMAL(10, 2),
        },
    )
