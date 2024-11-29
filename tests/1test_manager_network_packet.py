import unittest

from Manager.network.Packets.AuthPacket import AuthPacket

from Manager.network.Register import RegisterPacket


class TestNetWorkPacket(unittest.TestCase):
    
    def test_create_packet(self):
        auth = AuthPacket("artem-goooood")
        
        
        RegisterPacket().register(auth)


        print(auth.getId(), codec := auth.getCodec())
        byt = codec.encode()
        print( f"Сериализованные данные: {byt} " )

        # Wooot
        # -------------------------------------------------
        # byt -> отпровляютсяя сервером наверное так {"Packet": "Name", "data": byt, "Size": len(byt)}

        tests = RegisterPacket().get_codec(auth.getId())

        decoded_values = tests.decode(byt, 0)
        decoded_payload = tests.mainclass(*decoded_values)
        print(f"Десериализованные данные: password = {decoded_payload.getPassword()}, {decoded_payload.getINT()}")
        # self.assertEqual()
