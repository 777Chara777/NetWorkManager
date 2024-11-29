from abc import ABC, abstractmethod

class CustomCompression(ABC):
    ""
    
    @staticmethod
    @abstractmethod
    def compress(self, data: bytes) -> bytes:
        """
        Метод для сжатия данных.
        """

    @staticmethod
    @abstractmethod
    def decompress(self, data: bytes) -> bytes:
        """
        Метод для распаковки данных.
        """