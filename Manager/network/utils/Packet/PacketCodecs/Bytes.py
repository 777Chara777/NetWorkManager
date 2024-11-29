from Manager.network.utils.Packet.typings.Codec import Codec

class Bytes(Codec):

    @staticmethod
    def encode(value: bytes) -> bytes:
        length = len(value).to_bytes(4, 'big')
        return length + value

    @staticmethod
    def decode(buffer: bytes, offset: int) -> tuple:
        length = int.from_bytes(buffer[offset:offset+4], 'big')
        offset += 4
        value = buffer[offset:offset+length]
        return value, offset + length