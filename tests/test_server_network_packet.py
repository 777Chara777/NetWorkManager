import unittest

from Packets.HandShakePacket import HandShakePacket

from Manager.network.Register import RegisterPacket
from Manager import format_packet


class TestNetWorkPacket(unittest.TestCase):
    
    def test_create_packet(self):
        
        RegisterPacket().register( HandShakePacket )

        hsp = HandShakePacket((2, 225), b"01")
        # print( data := hsp.getCodec().encode(hsp) )  # b'\x00\x00\x00\x02\x00\x00\x00\xe1'
        # print( packet_data := data_format(hsp, data) )  # HandShakePacket,b'\x00\x00\x00\x02\x00\x00\x00\xe1',8      
        packet_data = format_packet( hsp, hsp.getCodec().encode(hsp) )
        
        # NetWork ---------

        packet, byte_data, data_size = packet_data.split(",")
        
        print(f"Size of byte data: {data_size} bytes")  # Size of byte data: 8 bytes

        packet = RegisterPacket().get_codec(packet)
        byte_data = bytes.fromhex(byte_data) 

        # print( handshack := packet.mainclass(*packet.decode(byte_data, 0)) ) 
        handshack = packet.mainclass(*packet.decode(byte_data, 0))
        # print( handshack.getOpenKey(), handshack.getSalt(), handshack.getId() )  # 2 225 HandShakePacket

        self.assertEqual( f"{hsp.getOpenKey(), hsp.getSalt(), hsp.getId()}", f"{handshack.getOpenKey(), handshack.getSalt(), handshack.getId()}" )