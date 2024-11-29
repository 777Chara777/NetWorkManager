import unittest

from Manager import Logger
from Manager import RegisterPacket

from Packets.AuthPacket import AuthPacket

class TestSingleton(unittest.TestCase):
    

    def test_singleton(self):
        logger = Logger("Main")
        RegisterPacket().register(AuthPacket)
        logger2 = Logger("test2")

        print(logger2.name)
        print(RegisterPacket().get_codec("AuthPacket"))
        print(logger.name)
