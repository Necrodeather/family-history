from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.base import email_sql, password, str_64

from .mixins import BaseMixin, CreatedAtMixin


class User(BaseMixin, CreatedAtMixin):
    __tablename__ = 'user'

    first_name: Mapped[str_64]
    last_name: Mapped[str_64]
    email: Mapped[email_sql] = mapped_column(unique=True)
    password: Mapped[password]
