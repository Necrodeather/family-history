class CredentialsError(Exception):
    def __init__(self) -> None:
        self.message = 'Could not validate credentials'
        super().__init__(self.message)


class IncorrectLoginError(Exception):
    def __init__(self) -> None:
        self.message = 'Incorrect login or password'
        super().__init__(self.message)


class NotFoundError(Exception):
    def __init__(self) -> None:
        self.message = 'Not Found'
        super().__init__(self.message)


class UserAlreadyRegisteredError(Exception):
    def __init__(self) -> None:
        self.message = 'A user with this email already exists'
        super().__init__(self.message)


class EntityAlreadyError(Exception):
    def __init__(self) -> None:
        self.message = 'A entity already exists'
        super().__init__(self.message)
