import socket

from threading import Thread

from Manager.utility.Logger.logger import Logger

class IClient:
    def __init__(self, ip: str, port: int) -> None:
        self.logger = Logger("NetWork-Client")

        self.__isconnect: bool = False
        self._socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.addres = (ip, port)

        self.thread: Thread

    def set_header(self, funciton, cls, deamon=True):
        if self.isopen():
            self.thread = Thread(target=funciton, name="lisen", args=(cls, ), daemon=deamon)
            self.thread.start()

    def connect(self) -> None:
        try:
            self._socket.connect(self.addres)
            self.logger.debug("Connection successful!")
            self.__isconnect = True
        except Exception as ex:
            self.logger.error(f"Connect to server fail :/ ({self.addres})\n - {ex}")

    def close(self) -> None:
        if self.isopen():
            self.logger.debug("Close Session")
            self._socket.close()
            self.__isconnect = False

    def isopen(self) -> bool:
        return self.__isconnect

    def sendto(self, data: bytes) -> None:
        if self.isopen():
            self._socket.send(data)
            self.logger.debug(f"Send Packet size: {len( data )} bytes")
        else:
            self.logger.warm("Connection to server not closed, message cannot be sent")

    def recv(self, bufsize: int) -> bytes:
        return self._socket.recv(bufsize)