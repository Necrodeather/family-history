import uuid

import factory

from app.domain.entities.auth import JWTUser


class JWTUserFactory(factory.Factory):
    class Meta:
        model = JWTUser

    id = str(uuid.uuid4())
    email = factory.Faker('ascii_free_email')
