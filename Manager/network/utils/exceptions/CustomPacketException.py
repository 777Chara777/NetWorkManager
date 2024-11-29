
class CustomPacketException(Exception):
    """Base class for exceptions related to CustomPackets."""
    def __init__(self, message: str):
        """
        Initializes a packet exception.

        Args:
            message (str): The error message describing the exception.
        """
        super().__init__(message)

    def __str__(self):
        base_message = super().__str__()
        print(base_message)
        return f"{self.__class__.__weakref__.__objclass__.__name__}:{self.__class__.__name__}"
        # if self.packet_type:
        #     return f"{base_message}:{self.packet_type.__name__}"
        # return base_message