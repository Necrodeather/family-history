import random

import factory
from faker import Faker

from app.public.api.schemas import (
    BudgetQueryApi,
    CategoryQueryApi,
    UserQueryApi,
)

faker = Faker()


class CategoryQueryApiFactory(factory.Factory):
    class Meta:
        model = CategoryQueryApi
        rename = {'name': 'name__like'}

    name = random.choice([faker.pystr(), None])
    page = random.choice([random.randint(1, 5), None])
    order = random.choice(['-name', 'name'])


class BudgetQueryApiFactory(factory.Factory):
    class Meta:
        model = BudgetQueryApi
        rename = {'name': 'name__like'}

    name = random.choice([faker.pystr(), None])
    category_id = random.choice([faker.pystr(), None])
    user_id = random.choice([faker.pystr(), None])
    page = random.choice([random.randint(1, 5), None])
    order = f"{random.choice(['-', ''])}{random.choice(
            ['name',
            'category_id',
            'user_id',
            ]
        )
    }"


class UserQueryApiFactory(factory.Factory):
    class Meta:
        model = UserQueryApi
        rename = {'name': 'name__like'}

    name = random.choice([faker.pystr(), None])
    page = random.choice([random.randint(1, 5), None])
    order = random.choice(['-name', 'name'])
