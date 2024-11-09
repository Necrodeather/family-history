from sqlalchemy.orm import Mapped

from .mixins import BaseMixin, CreatedAtMixin
from app.infrastructure.base import str_64, password, email, phone


class User(BaseMixin, CreatedAtMixin):
    __tablename__ = "users"

    first_name: Mapped[str_64]
    last_name: Mapped[str_64]
    phone_number: Mapped[phone]
    email: Mapped[email]
    password: Mapped[password]
