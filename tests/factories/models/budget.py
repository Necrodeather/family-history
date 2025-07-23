import uuid
from datetime import date

import factory

from app.infrastructure.database.models.budget import (
    Budget,
    Category,
    Expenses,
    ExpensesCategory,
    Income,
    IncomesCategory,
)

from .mixins import (
    BaseMixinFactory,
    CreatedAtMixinFactory,
    UpdatedAtMixinFactory,
)


class CategoryFactory(
    BaseMixinFactory,
    CreatedAtMixinFactory,
    UpdatedAtMixinFactory,
):
    class Meta:
        model = Category
        abstract = True

    name = factory.Faker('name')
    user_id = str(uuid.uuid4())
    updated_user_id = str(uuid.uuid4())


class ExpensesCategoryFactory(CategoryFactory):
    class Meta:
        model = ExpensesCategory

    expenses = factory.RelatedFactoryList(
        factory='tests.factories.models.budget.ExpensesFactory',
        factory_related_name='category',
        size=5,
    )


class IncomesCategoryFactory(CategoryFactory):
    class Meta:
        model = IncomesCategory

    incomes = factory.RelatedFactoryList(
        factory='tests.factories.models.budget.IncomeFactory',
        factory_related_name='category',
        size=5,
    )


class BudgetFactory(
    BaseMixinFactory,
    CreatedAtMixinFactory,
    UpdatedAtMixinFactory,
):
    class Meta:
        model = Budget
        abstract = True

    name = factory.Faker('name')
    amount = factory.Faker('pydecimal')
    date = factory.LazyFunction(date.today)
    user_id = str(uuid.uuid4())
    updated_user_id = str(uuid.uuid4())


class ExpensesFactory(BudgetFactory):
    class Meta:
        model = Expenses

    category_id = str(uuid.uuid4())
    category = factory.SubFactory(
        'tests.factories.models.budget.ExpensesCategoryFactory'
    )


class IncomeFactory(BudgetFactory):
    class Meta:
        model = Income

    category_id = str(uuid.uuid4())
    category = factory.SubFactory(
        'tests.factories.models.budget.IncomesCategoryFactory'
    )
