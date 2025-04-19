
from .CustomPacketException import CustomPacketException

class MissingCodecError(CustomPacketException):
    """Exception raised when a codec is missing for a packet."""
    def __init__(self, message: str):
        super().__init__(message)