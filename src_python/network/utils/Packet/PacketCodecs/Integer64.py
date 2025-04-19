from Manager.network.utils.Packet.typings.Codec import Codec

class Integer64(Codec):

    @staticmethod
    def encode(value: int) -> bytes:
        return value.to_bytes(64, 'big')

    @staticmethod
    def decode(buffer: bytes, offset: int) -> int:
        value = int.from_bytes(buffer[offset:offset+64], 'big')
        return value, offset + 64