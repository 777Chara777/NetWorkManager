from abc import ABC, abstractmethod

from typing import Any

class Codec(ABC):

    @staticmethod
    @abstractmethod
    def encode(value: str) -> bytes:
        """Method for serializing a value"""

    @staticmethod
    @abstractmethod
    def decode(buffer: bytes, offset: int) -> Any:
        """Method for deserializing a value"""