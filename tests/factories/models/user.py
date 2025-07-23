import factory
from passlib.context import CryptContext
from sqlalchemy_utils import Password

from app.infrastructure.database.models.user import User

from .mixins import BaseMixinFactory, CreatedAtMixinFactory

pwd_context = CryptContext(schemes=['pbkdf2_sha512'], deprecated='auto')


def _create_password(plain: str) -> Password:
    password =  Password(
        value=pwd_context.hash(plain),
        context=pwd_context,
    )
    password.test_password = plain
    return password


class UserFactory(BaseMixinFactory, CreatedAtMixinFactory):
    class Meta:
        model = User
        exclude = ('raw_password',)

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('ascii_free_email')
    raw_password = factory.Faker('password')

    @factory.lazy_attribute
    def password(self) -> Password:
        return _create_password(self.raw_password)
