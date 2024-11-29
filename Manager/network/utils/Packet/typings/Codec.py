from abc import ABC, abstractmethod

from typing import Any

class Codec(ABC):

    @staticmethod
    @abstractmethod
    def encode(value: str) -> bytes:
        """Метод для сериализации значения"""

    @staticmethod
    @abstractmethod
    def decode(buffer: bytes, offset: int) -> Any:
        """Метод для десериализации значения"""