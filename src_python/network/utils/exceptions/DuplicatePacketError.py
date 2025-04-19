
from .CustomPacketException import CustomPacketException

class DuplicatePacketError(CustomPacketException):
    """Exception raised when attempting to register a duplicate packet."""
    def __init__(self, message: str):
        super().__init__(message)