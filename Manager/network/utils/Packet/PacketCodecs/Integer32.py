from Manager.network.utils.Packet.typings.Codec import Codec

class Integer32(Codec):

    @staticmethod
    def encode(value: int) -> bytes:
        return value.to_bytes(32, 'big')

    @staticmethod
    def decode(buffer: bytes, offset: int) -> int:
        value = int.from_bytes(buffer[offset:offset+32], 'big')
        return value, offset + 32