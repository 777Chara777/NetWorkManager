from Manager.network.utils.Packet.typings.Codec import Codec

class String(Codec):

    @staticmethod
    def encode(value: str) -> bytes:
        encoded_str = value.encode('utf-8')
        length = len(encoded_str)
        return length.to_bytes(2, 'big') + encoded_str
    
    @staticmethod
    def decode(buffer: bytes, offset: int) -> str:
        length = int.from_bytes(buffer[offset:offset+2], 'big')
        value = buffer[offset+2:offset+2+length].decode('utf-8')
        return value, offset + 2 + length