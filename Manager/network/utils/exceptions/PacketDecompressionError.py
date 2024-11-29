
from .CustomPacketException import CustomPacketException

class PacketDecompressionError(CustomPacketException):
    """Exception raised when an error occurs during packet decompression."""
    def __init__(self, message="Error decompression packet data"):
        super().__init__(message)