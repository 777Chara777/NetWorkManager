import socket
import asyncio

from Manager.utility.Logger.logger import Logger
from Manager.network.utils.User import User


class IServer:
    def __init__(self, ip: str, port: int) -> None:
        self.logger = Logger("NetWork-Server")
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._mainloop = asyncio.new_event_loop()

        self.addres = (ip, port)

        self.__func_handle_accept: function = None

    def set_handle_accept(self, func):
        self.logger.debug("set handle accept")
        self.__func_handle_accept = func

    async def recv(self, client: socket.socket, nbytes: int = 1024) -> bytes:
        try:
            return await self._mainloop.sock_recv(client, nbytes)
        except ConnectionResetError as ex:
            self.logger.warm(f"Connection break! ..\n - {client=}")
            return b''

    async def client_accept(self) -> User:
        c, a = await self._mainloop.sock_accept(self._socket)
        return User( c, a, self )

    def bind(self):
        self.logger.info(f"Server Start at {self.addres}")
        self._socket.bind(self.addres)
        self._socket.listen(-1)
        self._socket.setblocking(False)

        if self.__func_handle_accept is None:
            self._socket.close()
            self._mainloop.close()
            self.logger.error("Определити handle client")
            raise Exception("Определити handle client")
        
        self._mainloop.run_until_complete(self.__func_handle_accept())

        
    async def send_to(self, data: bytes, address: "socket._RetAddress"):
        self.logger.debug(f"Send Packet size: {len( data )} bytes")
        await self._mainloop.sock_sendall(address, data)

    def create_task(self, coro, *, name=None, context=None):
        self._mainloop.create_task(coro, name=name, context=context)
        