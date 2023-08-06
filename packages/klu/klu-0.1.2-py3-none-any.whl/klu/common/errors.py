class UnknownKluError(Exception):
    def __init__(self):
        self.message = "Unknown error in Klu SDK. Please contact the support team."
        super().__init__(self.message)


class UnknownKluAPIError(Exception):
    def __init__(self, status: int, message: str):
        self.message = (
            f"Unknown error in Klu API.\nstatus_code: {status},\nmessage: {message}"
        )
        super().__init__(self.message)


class UnauthorizedError(Exception):
    def __init__(self):
        self.message = (
            f"Wrong credentials used to access the API. "
            f"Please, check you set the correct API key or contact the support team."
        )
        super().__init__(self.message)


class BadRequestAPIError(Exception):
    def __init__(self, status: int, message: str):
        self.message = (
            f"BadRequest error in Klu API.\nstatus_code: {status},\nmessage: {message}"
        )
        super().__init__(self.message)
