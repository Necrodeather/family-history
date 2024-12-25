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
