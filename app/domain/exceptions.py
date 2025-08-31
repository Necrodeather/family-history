class CredentialsError(Exception):
    """Raised when credentials cannot be validated."""

    def __init__(self) -> None:
        """Initializes the exception."""
        self.message = 'Could not validate credentials'
        super().__init__(self.message)


class IncorrectLoginError(Exception):
    """Raised when the login or password is incorrect."""

    def __init__(self) -> None:
        """Initializes the exception."""
        self.message = 'Incorrect login or password'
        super().__init__(self.message)


class NotFoundError(Exception):
    """Raised when an entity is not found."""

    def __init__(self) -> None:
        """Initializes the exception."""
        self.message = 'Not Found'
        super().__init__(self.message)


class UserAlreadyRegisteredError(Exception):
    """Raised when a user with the same email already exists."""

    def __init__(self) -> None:
        """Initializes the exception."""
        self.message = 'A user with this email already exists'
        super().__init__(self.message)


class EntityAlreadyError(Exception):
    """Raised when an entity already exists."""

    def __init__(self) -> None:
        """Initializes the exception."""
        self.message = 'A entity already exists'
        super().__init__(self.message)
