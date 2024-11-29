import unittest
from Manager import RegisterPacket
# from Manager.network.utils.exceptions.DuplicatePacketError import DuplicatePacketError
from Packets.PingPacket import PingPacket

class TestRegisterPacket(unittest.TestCase):
    def setUp(self):
        """Настройка тестов: создаем экземпляр RegisterPacket"""
        self.register = RegisterPacket()

    def test_register_packet(self):
        """Тест успешной регистрации пакета"""
        self.register.register(PingPacket)
        # self.assertIn(PingPacket, self.register._packets, "PingPacket не был зарегистрирован!")
        self.assertIsNotNone(self.register.get_codec(PingPacket.getId()) , "PingPacket не был зарегистрирован!")

    # def test_register_duplicate_packet(self):
    #     """Тест регистрации дублирующегося пакета"""
    #     self.register.register(PingPacket)
    #     with self.assertRaises(DuplicatePacketError, msg="Дублирующийся пакет был зарегистрирован!"):
    #         self.register.register(PingPacket)
