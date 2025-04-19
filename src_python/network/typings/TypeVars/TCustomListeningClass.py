from Manager.network.typings.CustomListeningClass import CustomListeningClass

from typing import TypeVar

__all__ = (
    "TCustomListeningClass",
)

TCustomListeningClass = TypeVar("TCustomListeningClass", bound=CustomListeningClass)
