from dependency_injector import containers, providers

from domain.entities.user import UserRead
from infrastructure.database.engine import SqlAlchemyEngine
from infrastructure.database.filter.user import UserFilter
from infrastructure.database.models.user import User
from infrastructure.database.repository.user import (
    AuthRepository,
    UserRepository,
)
from services.user import AuthService, UserService


class UserContainer(containers.DeclarativeContainer):
    """Container for user-related dependencies."""

    database_config = providers.Configuration()

    db: providers.Provider[SqlAlchemyEngine] = providers.Resource(
        SqlAlchemyEngine,
        uri=database_config.uri,
        echo=database_config.echo,
    )

    filter: providers.Provider[UserFilter] = providers.Factory(
        UserFilter,
        model=User,
    )

    repository: providers.Provider[UserRepository] = providers.Factory(
        UserRepository,
        engine=db,
        model=User,
        filter=filter,
    )

    service: providers.Provider[UserService] = providers.Factory(
        UserService,
        repository=repository,
        read_entity=UserRead,
    )


class AuthContainer(containers.DeclarativeContainer):
    """Container for authentication-related dependencies."""

    database_config = providers.Configuration()

    db: providers.Provider[SqlAlchemyEngine] = providers.Resource(
        SqlAlchemyEngine,
        uri=database_config.uri,
        echo=database_config.echo,
    )

    repository: providers.Provider[AuthRepository] = providers.Factory(
        AuthRepository,
        engine=db,
        model=User,
        filter=None,
    )

    service: providers.Provider[AuthService] = providers.Factory(
        AuthService,
        repository=repository,
        read_entity=UserRead,
    )
