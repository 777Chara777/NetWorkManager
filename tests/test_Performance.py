import timeit
import unittest

from Manager.network.Register import RegisterPacket
from Packets.PingPacket import PingPacket

class TestPerformance(unittest.TestCase):
    def test_register_performance(self):
        """Тест производительности регистрации пакетов"""
        def register_packet():
            register = RegisterPacket()
            register.register(PingPacket)

        execution_time = timeit.timeit(register_packet, number=1000)
        self.assertLess(execution_time, 1, "Регистрация пакетов занимает слишком много времени!")
