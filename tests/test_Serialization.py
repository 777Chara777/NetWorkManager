import unittest

from Packets.HandShakePacket import HandShakePacket

class TestSerialization(unittest.TestCase):    
    def test_packet_serialization(self):
        """Тест сериализации и десериализации пакета"""
        packet = HandShakePacket((11111,1105409645056505050560456065065), b"01")
        _encode = packet.getCodec().encode(packet)
        _decode = HandShakePacket(*HandShakePacket.getCodec().decode(_encode, 0))
        

        self.assertEqual(packet.__dict__, _decode.__dict__, "Сериализация/десериализация нарушила данные пакета!")
