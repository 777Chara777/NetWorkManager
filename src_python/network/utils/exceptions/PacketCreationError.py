
from .CustomPacketException import CustomPacketException

class PacketCreationError(CustomPacketException):
    """Raised when an error occurs while creating a packet."""
    def __init__(self, message="Error creating packet"):
        super().__init__(message)