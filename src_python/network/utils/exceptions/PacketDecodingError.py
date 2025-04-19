
from .CustomPacketException import CustomPacketException

class PacketDecodingError(CustomPacketException):
    """Exception raised when an error occurs during packet decoding."""
    def __init__(self, message="Error decoding packet data"):
        super().__init__(message)