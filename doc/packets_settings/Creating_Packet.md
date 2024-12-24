# Creating Packets

This document provides a detailed guide on how to create and use packets in the system. Packets are used to transmit data between a client and a server. Each packet must extend the `CustomPacket` class and implement its abstract methods.

## Example: HandShakePacket

Below is an example of creating a simple handshake packet.

### HandShakePacket Class

```python
from Manager.network.utils.Packet.CustomPacket import CustomPacket
from Manager.network.utils.Packet.PacketCodec import PacketCodec

class HandShakePacket(CustomPacket):
    # The `HandShakePacket` class is a custom packet that contains an open key and a salt. It extends the `CustomPacket` class and implements its required methods.
    
    def __init__(self, openkey: tuple[int, int], salt: bytes) -> None:
        self.openkey: tuple[int, int] = openkey
        self.salt:    bytes           = salt

    @staticmethod
    def getId() -> str:
        # This method returns a unique identifier for the packet type. It is used to distinguish between different types of packets in the system.
        
        return "HandShakePacket"

    def get_salt(self) -> bytes:
        # This method returns the salt value of the packet.
        
        return self.salt

    def get_openkey(self) -> tuple[int, int]:
        # This method returns the open key of the packet.
        
        return self.openkey

    @staticmethod
    def getCodec() -> PacketCodec:
        # This method returns an instance of `PacketCodec`, which is responsible for encoding and decoding the packet's data. The `PacketCodec` is initialized with the packet class and the fields to be encoded/decoded.

        return PacketCodec(
            HandShakePacket, 
            (PacketCodecs.Tuple(PacketCodecs.Integer, PacketCodecs.Integer128), get_openkey),
            (PacketCodecs.Bytes, get_salt)
        )
```

- [PacketCodecs](/Manager/network/utils/Packet/PacketCodecs/): This is a set of classes that are used to encode and decode different types of data in packets. [Example](./packetscodec/PacketsCodecs.md)

### Summary

- **`getId`**: Returns a unique identifier for the packet type.
- **`get_salt`**: Returns the salt value of the packet.
- **`get_openkey`**: Returns the open key of the packet.
- **`getCodec`**: Returns a `PacketCodec` instance that defines how the packet is serialized and deserialized.
- **`getCompression`**: Returns a `CustomCompression` instance that defines how the packet is compressed and decompressed.

---

To see the structure of creating packets, follow the interface: [CustomPacket](/Manager/network/utils/Packet/CustomPacket.py)

### Brief Example of CustomPacket Structure

```python
class CustomPacket(ABC):

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
```
