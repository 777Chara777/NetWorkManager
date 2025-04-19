from Manager.network.utils.Packet.typings.Codec import Codec

class Integer(Codec):

    @staticmethod
    def encode(value: int) -> bytes:
        return value.to_bytes(4, 'big')

    @staticmethod
    def decode(buffer: bytes, offset: int) -> int:
        value = int.from_bytes(buffer[offset:offset+4], 'big')
        return value, offset + 4