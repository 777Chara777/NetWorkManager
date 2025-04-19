from Manager.utility.classes.Singleton import Singleton

from Manager.network.utils.Packet.CustomPacket import CustomPacket
from Manager.network.utils.Packet.PacketCodec import PacketCodec
from Manager.network.utils.Packet.typings.Packet import Packet

from Manager.network.typings.CustomListeningClass import CustomListeningClass
from Manager.network.typings.TypeVars.TCustomListeningClass import TCustomListeningClass
from Manager.network.typings.TypeVars.TCustomPacket import TCustomPacket

# from Manager.network.utils.exceptions.DuplicatePacketError import DuplicatePacketError

from Manager.network.utils.User import User

from typing import Self, overload

class RegisterPacket(metaclass=Singleton):
    def __init__(self) -> None:
        self._packets: dict[str, TCustomPacket] = {}
    
    @overload
    def register(self, *packets: tuple[TCustomPacket, TCustomListeningClass]):
        """
        Overloaded method for registering a packet along with an event listener class.

        Parameters:
            packets (tuple[TCustomPacket, TCustomListeningClass]): containing a CustomPacket class and a corresponding event listener class.
        """

    @overload
    def register(self, *packets: TCustomPacket):
        """
        Overloaded method for registering only packet classes.

        Parameters:
            packets (CustomPacket): classes that will be registered.
        """


    def register(self, *packets):
        """
        Registers packets or packets with event listeners into the system. 

        For each packet:
        - If a tuple of (packet, listener) is provided, it registers the packet and its corresponding event listener.
        - If only a packet is provided, it registers the packet alone.
        - Ensures that the packet inherits from CustomPacket.
        - If the packet ID is already registered, the registration is skipped.

        Parameters:
            packets: A variable number of packet classes or tuples of packet classes and event listeners.

        Raises:
            ValueError: If the packet class does not inherit from CustomPacket.
            DuplicatePacketError: duplicate packet registration detected.
        """
        for packet in packets:
            
            # if not isinstance(packet, type):
            #     raise TypeError(f"Переданный объект {packet} не является классом")
            
            if isinstance(packet, tuple):
                ListeningEvents().register(packet[0], packet[1])
                packet = packet[0]

            if not issubclass(packet, CustomPacket):
                raise ValueError(f"Packet '{packet.__name__}' does not inherit from class CustomPacket")
            if packet.getId() in self._packets:
                # raise DuplicatePacketError(f"Duplicate packet registration detected for {packet.getId()}.")
                break
            self._packets[packet.getId()] = packet.getCodec()

    def get_codec(self, id: str) -> PacketCodec | None:
        return self._packets.get(id, None)
    
class ListeningEvents(metaclass=Singleton):
    def __init__(self) -> None:
        self._events: dict[str, TCustomListeningClass] = {}

    def register(self, packet: TCustomPacket, _class: TCustomListeningClass):
        self._events[packet.getId()] = _class()

    def get_events(self) -> list[str]:
        return list(self._events.keys())
    
    @staticmethod
    async def call_event(cls: Self, event: str, packet: Packet, user: User):
        await ListeningEvents()._events.get(event).call(cls, packet, user)

    @staticmethod
    def no_call_event(cls: Self, event: str, packet: Packet):
        ListeningEvents()._events.get(event).no_call(cls, packet)