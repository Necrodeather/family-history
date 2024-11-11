from sqlalchemy.orm import Mapped, mapped_column

from .mixins import BaseMixin, CreatedAtMixin
from app.infrastructure.base import str_64, password, email_sql


class User(BaseMixin, CreatedAtMixin):
    __tablename__ = "users"

    first_name: Mapped[str_64]
    last_name: Mapped[str_64]
    email: Mapped[email_sql] = mapped_column(unique=True)
    password: Mapped[password]
