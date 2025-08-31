from dependency_injector import containers, providers

from domain.entities.category import CategoryRead
from infrastructure.database.engine import SqlAlchemyEngine
from infrastructure.database.filter.budget import CategoryFilter
from infrastructure.database.models.category import (
    ExpensesCategory,
    IncomesCategory,
)
from infrastructure.database.repository.category import (
    ExpensesCategoryRepository,
    IncomesCategoryRepository,
)
from services.category import CategoryService


class ExpensesCategoryContainer(containers.DeclarativeContainer):
    """Container for expenses category-related dependencies."""

    database_config = providers.Configuration()

    db: providers.Provider[SqlAlchemyEngine] = providers.Resource(
        SqlAlchemyEngine,
        uri=database_config.uri,
        echo=database_config.echo,
    )

    filter: providers.Provider[CategoryFilter] = providers.Factory(
        CategoryFilter,
        model=ExpensesCategory,
    )

    repository: providers.Provider[ExpensesCategoryRepository] = (
        providers.Factory(
            ExpensesCategoryRepository,
            engine=db,
            model=ExpensesCategory,
            filter=filter,
        )
    )

    service: providers.Provider[CategoryService] = providers.Factory(
        CategoryService,
        repository=repository,
        read_entity=CategoryRead,
    )


class IncomesCategoryContainer(containers.DeclarativeContainer):
    """Container for incomes category-related dependencies."""

    database_config = providers.Configuration()

    db: providers.Provider[SqlAlchemyEngine] = providers.Resource(
        SqlAlchemyEngine,
        uri=database_config.uri,
        echo=database_config.echo,
    )

    filter: providers.Provider[CategoryFilter] = providers.Factory(
        CategoryFilter,
        model=IncomesCategory,
    )

    repository: providers.Provider[IncomesCategoryRepository] = (
        providers.Factory(
            IncomesCategoryRepository,
            engine=db,
            model=ExpensesCategory,
            filter=filter,
        )
    )

    service: providers.Provider[CategoryService] = providers.Factory(
        CategoryService,
        repository=repository,
        read_entity=CategoryRead,
    )
