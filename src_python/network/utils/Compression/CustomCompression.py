from abc import ABC, abstractmethod

class CustomCompression(ABC):
    ""
    
    @staticmethod
    @abstractmethod
    def compress(self, data: bytes) -> bytes:
        """
        A method for compressing data.
        """

    @staticmethod
    @abstractmethod
    def decompress(self, data: bytes) -> bytes:
        """
        Method for decompressing data.
        """