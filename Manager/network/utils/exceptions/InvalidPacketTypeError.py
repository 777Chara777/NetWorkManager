
from .CustomPacketException import CustomPacketException

class InvalidPacketTypeError(CustomPacketException):
    """Exception raised when an invalid packet type is used."""
    def __init__(self, message: str):
        super().__init__(message)