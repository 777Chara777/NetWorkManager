from Manager.network.utils.Packet.typings.Packet import Packet
from Manager.network.utils.User import User

from typing import Self

class CustomListeningClass:
    async def call(self: Self, cls: Self, packet: Packet, user: User): ...
    def no_call(self: Self, cls: Self, packet: Packet): ...