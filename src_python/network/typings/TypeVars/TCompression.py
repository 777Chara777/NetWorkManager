from Manager.network.utils.Compression.CustomCompression import CustomCompression
# from Manager.network.utils.Packet.CustomPacket import CustomPacket

from typing import TypeVar

__all__ = (
    "TCompression",
)

TCompression = TypeVar("TCompression", bound=CustomCompression)
