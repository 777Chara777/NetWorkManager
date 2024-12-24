```python
from Manager.network.utils.Packet.CustomPacket import CustomPacket
from Manager.network.utils.Packet.PacketCodec import PacketCodec

class ExamplePacket(CustomPacket):
    def __init__(self, message: str) -> None:
        self.message = message

    @staticmethod
    def getId() -> str:
        return "ExamplePacket"

    @staticmethod
    def getCodec() -> PacketCodec:
        return PacketCodec(
            ExamplePacket, 
            (PacketCodecs.String, lambda x: x.message)
        )
```
