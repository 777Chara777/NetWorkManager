import struct
import unittest

from Manager.utility.Logger.logger import Logger

from Manager import format_packet
from Packets.HandShakePacket import HandShakePacket

class TestStructEffect(unittest.TestCase):
    "Проверка на сколько эефективен модуль struct"

    # def test_logger_create(self):
    #     Logger("main")
    
    def test_struct_effect(self):
        logger = Logger("Test-struct")

        p = HandShakePacket((1,2), b'')

        data = p.getCodec().encode(p)
        # logger.debug(str(data))

        # f"{packet.getId()},{content},{len(content.encode('utf-8'))}"

        d = struct.pack(f">15s{len(data)}si", p.getId().encode(encoding="utf-8") , data, len(data.hex().encode('utf-8')))
        
        logger.info(format_packet(p, data))
        logger.info("struct.pack=", d.__sizeof__())
        logger.info("p.getCodec().encode(p)=", data.__sizeof__())
        # logger.info(struct.unpack(">15s1024si", d))

        self.assertFalse(d.__sizeof__() < data.__sizeof__(), "struct effective!")
        