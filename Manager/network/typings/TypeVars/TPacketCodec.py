

from Manager.network.utils.Packet.PacketCodec import PacketCodec

from typing import TypeVar

__all__ = (
    "TPacketCodec",
)

TPacketCodec = TypeVar("TPacketCodec", bound=PacketCodec)
