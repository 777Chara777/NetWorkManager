from Manager.network.utils.Packet.typings.Codec import Codec

class Tuple(Codec):
    def __init__(self, *codecs):
        self.codecs = codecs

    def encode(self, values: tuple) -> bytes:
        encoded = b''
        for codec, value in zip(self.codecs, values):
            encoded += codec.encode(value)
        return encoded

    def decode(self, buffer: bytes, offset: int) -> tuple:
        values = []
        for codec in self.codecs:
            value, offset = codec.decode(buffer, offset)
            values.append(value)
        return tuple(values), offset