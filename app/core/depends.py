from typing import Any

from dependency_injector import containers, providers

from app.domain.entities.budget import BudgetRead
from app.domain.entities.category import CategoryRead
from app.domain.entities.user import UserRead
from app.infrastructure.database.engine import SqlAlchemyEngine
from app.infrastructure.database.filter.budget import (
    BudgetFilter,
    CategoryFilter,
)
from app.infrastructure.database.filter.user import UserFilter
from app.infrastructure.database.models.budget import (
    Expenses,
    Income,
)
from app.infrastructure.database.models.category import (
    ExpensesCategory,
    IncomesCategory,
)
from app.infrastructure.database.models.user import User
from app.infrastructure.database.repository.budget import (
    ExpensesRepository,
    IncomeRepository,
)
from app.infrastructure.database.repository.category import (
    ExpensesCategoryRepository,
    IncomesCategoryRepository,
)
from app.infrastructure.database.repository.user import (
    AuthRepository,
    UserRepository,
)
from app.service.budget import BudgetService
from app.service.category import CategoryService
from app.service.user import AuthService, UserService


class ApiContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=['app.public.api.v1']
    )

    database_config = providers.Configuration()

    db: providers.Singleton[SqlAlchemyEngine] = providers.Singleton(
        SqlAlchemyEngine,
        uri=database_config.uri,
        echo=database_config.echo,
    )

    filter: providers.FactoryAggregate[Any] = providers.FactoryAggregate(
        expenses=providers.Factory(
            BudgetFilter,
            model=Expenses,
        ),
        income=providers.Factory(
            BudgetFilter,
            model=Income,
        ),
        expenses_category=providers.Factory(
            CategoryFilter,
            model=ExpensesCategory,
        ),
        income_category=providers.Factory(
            CategoryFilter,
            model=IncomesCategory,
        ),
        user=providers.Factory(
            UserFilter,
            model=User,
        ),
    )

    repository: providers.FactoryAggregate[Any] = providers.FactoryAggregate(
        expenses=providers.Factory(
            ExpensesRepository,
            engine=db,
            model=Expenses,
            filter=filter.expenses,
        ),
        income=providers.Factory(
            IncomeRepository,
            engine=db,
            model=Income,
            filter=filter.income,
        ),
        expenses_category=providers.Factory(
            ExpensesCategoryRepository,
            engine=db,
            model=ExpensesCategory,
            filter=filter.expenses_category,
        ),
        income_category=providers.Factory(
            IncomesCategoryRepository,
            engine=db,
            model=IncomesCategory,
            filter=filter.income_category,
        ),
        auth=providers.Factory(
            AuthRepository,
            engine=db,
            model=User,
            filter=filter.user,
        ),
        user=providers.Factory(
            UserRepository,
            engine=db,
            model=User,
            filter=filter.user,
        ),
    )

    service: providers.FactoryAggregate[Any] = providers.FactoryAggregate(
        expenses=providers.Factory(
            BudgetService,
            repository=repository.expenses,
            read_entity=BudgetRead,
        ),
        income=providers.Factory(
            BudgetService,
            repository=repository.income,
            read_entity=BudgetRead,
        ),
        expenses_category=providers.Factory(
            CategoryService,
            repository=repository.expenses_category,
            read_entity=CategoryRead,
        ),
        income_category=providers.Factory(
            CategoryService,
            repository=repository.income_category,
            read_entity=CategoryRead,
        ),
        auth=providers.Factory(
            AuthService,
            repository=repository.auth,
            read_entity=UserRead,
        ),
        user=providers.Factory(
            UserService,
            repository=repository.user,
            read_entity=UserRead,
        ),
    )

    expenses_service = service.expenses
    income_service = service.income
    expenses_category_service = service.expenses_category
    income_category_service = service.income_category
    auth_service = service.auth
    user_service = service.user
