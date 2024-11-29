import socket
from typing import TYPE_CHECKING

from Manager.utility.RSA.publickey import PublicKey

if TYPE_CHECKING:
    from Manager.network.Server import IServer

class User:
    def __init__(self, conn: socket.socket, address: "socket._RetAddress", server: "IServer") -> None:
        self.rsa: PublicKey = None
        self.__server = server
        self.connection = conn
        self.address = address

    def set_publickey(self, _rsa: PublicKey) -> None:
        if isinstance(_rsa, PublicKey):
            self.rsa = _rsa

    def ispublickey(self) -> bool:
        return not self.rsa is None


    def disconect(self):
        self.connection.close()
        
    async def sendto(self, data: bytes):
        return await self.__server.send_to(data, self.connection)


    def __contains__(self, address) -> bool:
        return address == self.address
    
