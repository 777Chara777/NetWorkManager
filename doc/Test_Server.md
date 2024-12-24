```python
from Manager import IServer, Logger, RegisterPacket, ListeningEvents
from Packets.HandShakePacket import HandShakePacket
from Server.events.HandShakeEvent import HandShakeEvent

class Server:
    def __init__(self) -> None:
        self.logger = Logger("Server")
        self.server = IServer("127.0.0.1", 25565)

        RegisterPacket().register(
            (HandShakePacket, HandShakeEvent)
        )

        self.server.set_handle_accept(self.handle_accept)

    async def handle_accept(self):
        while True:
            user = await self.server.client_accept()
            self.logger.info(f"New connection: {user.address}")

            self.server.create_task(self.handle_client(user))

    async def handle_client(self, user):
        while True:
            data = await self.server.recv(user.connection, 1024)
            if not data:
                self.logger.info(f"User disconnected: {user.address}")
                break

            packet = parse_packet(data.decode())
            if packet.packet.getId() in ListeningEvents().get_events():
                await ListeningEvents.call_event(self, packet.packet.getId(), packet, user)

    def run(self):
        self.server.bind()
        self.logger.info("Server started...")
```
