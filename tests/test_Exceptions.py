import unittest

from Manager.network.Register import RegisterPacket
from Packets.HandShakePacket import HandShakePacket

from Manager.network.utils.exceptions.PacketDecodingError import PacketDecodingError


class TestExceptions(unittest.TestCase):
    def setUp(self):
        """Настройка тестов: создаем экземпляр RegisterPacket"""
        self.register = RegisterPacket()
        self.register.register(HandShakePacket)
    
    def test_register_invalid_packet(self):
        """Тест регистрации неверного типа пакета"""
        with self.assertRaises(TypeError, msg="Ожидалось исключение TypeError при регистрации неправильного пакета!"):
            self.register.register(None)

    def test_packet_decoding_error(self):
        """Тест ошибки декодирования пакета"""
        with self.assertRaises(TypeError, msg="Ошибка buffer'а пакета!"):
            # Пример некорректного декодирования
            HandShakePacket.getCodec().decode("Hello, World!", 0)
        
        with self.assertRaises(TypeError, msg="Ошибка offset'а пакета!"):
            # Пример некорректного декодирования
            HandShakePacket.getCodec().decode(b"1", "")

        # with self.assertRaises(PacketDecodingError, msg="Ошибка декодирования пакета не была выброшена!"):
        #     # Пример некорректного декодирования
        #     HandShakePacket.getCodec().decode(b"\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x0201", 6)
