
from .CustomPacketException import CustomPacketException

class PacketEncodingError(CustomPacketException):
    """Exception raised when an error occurs during packet encoding."""
    def __init__(self, message: str):
        super().__init__(message)