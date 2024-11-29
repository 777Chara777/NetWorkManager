import unittest

from Manager.utility.Logger.logger import Logger


from Packets.HandShakePacket import HandShakePacket
from Packets.MessagePacket import MessagePacket
from Manager.network.Register import RegisterPacket


class TestComptess(unittest.TestCase):
    
    def compress_string(self, context: str) -> str:
        if not context:
            return ""
        
        # 0-8 > 9 -перенос
        # 91 -> 9
        # 93 -> 11
        # 8 ричная система 
        compressed = ["0"]
        i = 0
        while i < len(context) - 1:
            pair = context[i:i+2]
            count = 1
            while i + 2 < len(context) and context[i+2:i+4] == pair:
                count += 1
                i += 2
            if int(compressed[0]) < count:
                compressed[0] = str(count)
            compressed.append((count, pair,))
            i += 2

        if len(context) % 2 == 1:  # Добавляем последний символ, если длина нечётная
            compressed.append(context[-1])
        # logger.debug(len(compressed[0]))
        return f"{len(compressed[0])}"+"".join( [f"{str(n).zfill(len(compressed[0]))}{l}" for n, l in compressed[1:]] )
        # return compressed

    def decompress_string(self, compressed: str) -> str:
        size_group = int(compressed[0]) + 2
        compressed = compressed[1:]
        
        if not compressed:
            return ""
        
        decompressed = []
        for group in range(len(compressed) // size_group):
            it = group*size_group
            size, n = int(compressed[it:it+size_group-2]), compressed[it+size_group-2:it+size_group]
            decompressed.append( str(n) * size )
        
        return bytes.fromhex( "".join(decompressed) )



    def test_compress_v1(self):
        logger = Logger("Compress-V1")

        def compress_string(context: str) -> str:
            fun_mess = []
            it2 = 0
            for it in range(0, len(context), 2):
                if it != it2:
                    continue
                can = 0
                for it2 in range(it, len(context), 2):
                    if f"{context[it]+context[it+1]}" != f"{context[it2]+context[it2+1]}":
                        break
                    can +=1
            
                fun_mess.append(f"{can}{context[it]+context[it+1]}")
            # logger.debug(fun_mess[:-1])
            return "".join(fun_mess[:-1])

        def decompress_string(context: str) -> str:
            
            pass

        # size > len([].encode('utf-8'))

        RegisterPacket().register( HandShakePacket )

        hsp = HandShakePacket((23450, 2555514504505444684056025), b"2555")

        logger.info(f"{(d := hsp.getCodec().encode(hsp).hex())=}")
        logger.info(f"- {len(d)=}")
        logger.info(f"{(ed := compress_string(d))=}")
        logger.info(f"- {len(ed)=}")


        # logger.info( d := format_packet( hsp, hsp.getCodec().encode(hsp).hex() ) )

        # logger.info( g :=  d.encode().hex() )
        # logger.info( bytes.fromhex(g) )

    
    def test_compress_v2(self):
        logger = Logger("Compress-V2")



        # size > len([].encode('utf-8'))

        RegisterPacket().register( HandShakePacket )


        hsp = HandShakePacket((145242785,845888754728754), b"05005450a0f6,fddddddd")
        
        logger.info(f"{(d := hsp.getCodec().encode(hsp))=}")
        logger.info(f"- {len(d)=}")
        logger.info(f"{(ed := self.compress_string(d.hex()))=}")
        logger.info(f"- {len(ed.encode('utf-8'))=}/{len(ed)}")
        logger.info(f"{(de := self.decompress_string(ed))=}")
        logger.info(f"- {len(de)=}")
        c = (len(d) / len(ed.encode('utf-8')))
        logger.info("Сжатие в %s раз" % c)
        self.assertEqual(len(d), len(de), "Оно не поможет тебе выжить ааааааааааааааааааааааааааааааааааа")
        self.assertTrue(c > 0.4, "Он упал в жатии Аааааааааааа")
        # self.assertTrue(len(d) > len(ed.encode('utf-8')), "Хахахах нельзя использовать аогоритм!")

    def test_compress_v3(self):
        logger = Logger("Compress-V3")

        RegisterPacket().register( MessagePacket )

        hsp = MessagePacket("Странно когда я писал это сообщение прошло больше пакетов чем отправка точек :)))")

        logger.info(f"{(d := hsp.getCodec().encode(hsp))=}")
        logger.info(f"- {len(d)=}")
        logger.info(f"{(ed := self.compress_string(d.hex()))=}")
        logger.info(f"- {len(ed.encode('utf-8'))=}/{len(ed)}")
        logger.info(f"{(de := self.decompress_string(ed))=}")
        logger.info(f"- {len(de)=}")

        c = (len(d) / len(ed.encode('utf-8')))
        logger.info("Сжатие в %s раз" % c)

        self.assertEqual(len(d), len(de), "Оно не поможет тебе выжить ааааааааааааааааааааааааааааааааааа")
        # self.assertTrue(c > 0.4, "Он упал в жатии Аааааааааааа")

    def test_compress_in_packet(self):
        logger = Logger("Compress-in_packet")

        d = MessagePacket("Странно когда я писал это сообщение прошло больше пакетов чем отправка точек :)))")
        e = d.getCodec().encode(d)
        g = d.getCompression().compress(e.hex())
        v = d.getCompression().decompress(g)

        c = (len(e) / len(g.encode('utf-8')))
        logger.info("Сжатие в %s раз / %s, %s" % (c, len(e), len(g.encode("utf-8"))))

        self.assertEqual(len(e), len(v), "Оно не поможет тебе выжить ааааааааааааааааааааааааааааааааааа")
        self.assertTrue(c > 0.4, "Он упал в жатии Аааааааааааа")


# HandShakePacket -> "48616e645368616b655061636b6574" (hex)
# 2c -> "," (hex)
# 30 -> "0" (hex)

# 200 15b 19a 11700 10211d1261b810818719216714c1c51d9300104132335135