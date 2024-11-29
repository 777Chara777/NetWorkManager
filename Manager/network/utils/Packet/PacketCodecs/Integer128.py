from Manager.network.utils.Packet.typings.Codec import Codec

class Integer128(Codec):

    @staticmethod
    def encode(value: int) -> bytes:
        return value.to_bytes(128, 'big')

    @staticmethod
    def decode(buffer: bytes, offset: int) -> int:
        value = int.from_bytes(buffer[offset:offset+128], 'big')
        return value, offset + 128