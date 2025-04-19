from abc import ABC, abstractmethod

from typing import TYPE_CHECKING

# from Manager.network.typings.TypeVars.TCompression import TCompression
# from Manager.network.typings.TypeVars.TPacketCodec import TPacketCodec

if TYPE_CHECKING:

    from .PacketCodec import PacketCodec
    from ..Compression.CustomCompression import CustomCompression

class CustomPacket(ABC):
    """
## `CustomPacket` Class

The `CustomPacket` class serves as an abstract base class for creating network packets. This class acts as an interface that must be extended by concrete implementations, ensuring consistency in how packets are identified and encoded.

### Overview

The `CustomPacket` class defines two essential static methods that every subclass must implement:

- **`getId()`**: This method returns a unique identifier for the packet. It is used to distinguish between different types of packets in the system.
- **`getCodec()`**: This method returns an instance of `PacketCodec`, which is responsible for encoding and decoding the packet's data.

By using `CustomPacket` as a parent class, you ensure that every packet type in your application has a consistent structure and can be seamlessly serialized and deserialized for network transmission.
    """
    
    @staticmethod
    @abstractmethod
    def getId() -> str:
        """
        Returns a unique identifier for the packet type.
        """

    @staticmethod
    @abstractmethod
    def getCodec() -> "PacketCodec": 
        """
        Returns a PacketCodec instance that defines how the packet is serialized and deserialized.
        """

    @staticmethod
    @abstractmethod
    def getCompression() -> "CustomCompression":
        """
        Returns a Compression instance that defines how the packet is serialized and deserialized.
        """