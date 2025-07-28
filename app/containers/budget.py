from dependency_injector import containers, providers

from domain.entities.budget import BudgetRead
from infrastructure.database.engine import SqlAlchemyEngine
from infrastructure.database.filter.budget import (
    BudgetFilter,
)
from infrastructure.database.models.budget import (
    Expenses,
    Income,
)
from infrastructure.database.repository.budget import (
    ExpensesRepository,
    IncomeRepository,
)
from service.budget import BudgetService


class ExpensesContainer(containers.DeclarativeContainer):
    database_config = providers.Configuration()

    db: providers.Provider[SqlAlchemyEngine] = providers.Resource(
        SqlAlchemyEngine,
        uri=database_config.uri,
        echo=database_config.echo,
    )

    filter: providers.Provider[BudgetFilter] = providers.Factory(
        BudgetFilter,
        model=Expenses,
    )

    repository: providers.Provider[ExpensesRepository] = providers.Factory(
        ExpensesRepository,
        engine=db,
        model=Expenses,
        filter=filter,
    )

    service: providers.Provider[BudgetService] = providers.Factory(
        BudgetService,
        repository=repository,
        read_entity=BudgetRead,
    )


class IncomeContainer(containers.DeclarativeContainer):
    database_config = providers.Configuration()

    db: providers.Provider[SqlAlchemyEngine] = providers.Resource(
        SqlAlchemyEngine,
        uri=database_config.uri,
        echo=database_config.echo,
    )

    filter: providers.Provider[BudgetFilter] = providers.Factory(
        BudgetFilter,
        model=Income,
    )

    repository: providers.Provider[IncomeRepository] = providers.Factory(
        IncomeRepository,
        engine=db,
        model=Income,
        filter=filter,
    )

    service: providers.Provider[BudgetService] = providers.Factory(
        BudgetService,
        repository=repository,
        read_entity=BudgetRead,
    )
