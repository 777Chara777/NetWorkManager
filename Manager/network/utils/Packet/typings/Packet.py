from dataclasses import dataclass
from Manager.network.typings.TypeVars.TCustomPacket import TCustomPacket

@dataclass()
class Packet:
    packet: TCustomPacket
    size: int
