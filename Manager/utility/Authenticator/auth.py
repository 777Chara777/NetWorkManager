

class Authenticator:
    def __init__(self, secret: str) -> None:
        self.__secret = secret

    def validate(self, code: str) -> bool:
        pass