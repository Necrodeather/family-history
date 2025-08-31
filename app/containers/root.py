from dependency_injector import containers, providers

from containers.budget import ExpensesContainer, IncomeContainer
from containers.category import (
    ExpensesCategoryContainer,
    IncomesCategoryContainer,
)
from containers.user import AuthContainer, UserContainer


class AppContainer(containers.DeclarativeContainer):
    """
    Root container for all application dependencies.
    """
    wiring_config = containers.WiringConfiguration(packages=['public.api.v1'])

    database_config = providers.Configuration()

    expenses = providers.Container(
        ExpensesContainer,
        database_config=database_config,
    )
    income = providers.Container(
        IncomeContainer,
        database_config=database_config,
    )
    expenses_category = providers.Container(
        ExpensesCategoryContainer,
        database_config=database_config,
    )
    incomes_category = providers.Container(
        IncomesCategoryContainer,
        database_config=database_config,
    )
    auth = providers.Container(
        AuthContainer,
        database_config=database_config,
    )
    user = providers.Container(
        UserContainer,
        database_config=database_config,
    )
