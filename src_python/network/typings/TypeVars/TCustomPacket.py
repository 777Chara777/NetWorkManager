from Manager.network.utils.Packet.CustomPacket import CustomPacket

from typing import TypeVar

__all__ = (
    "TCustomPacket",
)

TCustomPacket = TypeVar("TCustomPacket", bound=CustomPacket)
