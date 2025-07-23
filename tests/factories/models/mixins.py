import uuid
from datetime import datetime

import factory

from app.infrastructure.database.models.mixins import (
    BaseMixin,
    CreatedAtMixin,
    UpdatedAtMixin,
)


class BaseMixinFactory(factory.Factory):
    class Meta:
        model = BaseMixin
        abstract = True

    id = str(uuid.uuid4())


class CreatedAtMixinFactory(factory.Factory):
    class Meta:
        model = CreatedAtMixin
        abstract = True

    created_at = factory.LazyFunction(datetime.now)


class UpdatedAtMixinFactory(factory.Factory):
    class Meta:
        model = UpdatedAtMixin
        abstract = True

    updated_at = factory.LazyFunction(datetime.now)
