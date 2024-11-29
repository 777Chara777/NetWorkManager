### README

# Manager: Инструмент для работы с сетью

## Описание

**Manager** — это мощный инструмент, предназначенный для работы с сетевыми взаимодействиями. Он предоставляет разработчикам средства для создания как серверов, так и клиентов с использованием единого подхода на основе пакетов. **Manager** не является готовым сервером или клиентом, а служит гибкой базой для их разработки.

Основная идея заключается в создании стандартизированных пакетов, которые могут быть использованы для обмена данными между клиентами и серверами, а также в обработке событий.

---

## Основные возможности

1. **Регистрация пакетов**  
   Manager позволяет регистрировать пакеты и связанные с ними события, которые будут обрабатываться в процессе взаимодействия.

2. **Поддержка RSA**  
   Шифрование трафика осуществляется с помощью RSA, что обеспечивает безопасность передаваемых данных.

3. **Модульная архитектура**  
   - Система позволяет добавлять и обрабатывать пользовательские пакеты.  
   - Удобный инструмент для разделения задач между обработчиками событий и пакетами.

4. **Гибкость и масштабируемость**  
   Manager предоставляет базовые классы и методы, которые можно адаптировать для создания приложений любого масштаба.

---

## Пример использования

### Создание сервера

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

---

## Основные модули

- **RegisterPacket**  
  Регистрация пользовательских пакетов и событий.

- **ListeningEvents**  
  Обработка событий, связанных с пакетами.

- **CustomPacket**  
  Базовый класс для создания собственных пакетов.

- **RSA**  
  Утилита для шифрования данных.

- **Logger**  
  Удобная система логирования для отслеживания работы сервера и клиента.

---

## Пример регистрации пакета

```python
from Manager.network.utils.Packet.CustomPacket import CustomPacket
from Manager.network.utils.Packet.PacketCodec import PacketCodec

class HandShakePacket(CustomPacket):
    def __init__(self, openkey: tuple[int, int], salt: bytes) -> None:
        self.openkey = openkey
        self.salt = salt

    @staticmethod
    def getId() -> str:
        return "HandShakePacket"

    @staticmethod
    def getCodec() -> PacketCodec:
        return PacketCodec(
            HandShakePacket, 
            (PacketCodecs.Tuple(PacketCodecs.Integer, PacketCodecs.Integer128), lambda x: x.openkey),
            (PacketCodecs.Bytes, lambda x: x.salt)
        )
```

---

## Возможности расширения

- Легко добавить свои типы пакетов.
- Простое подключение собственных обработчиков событий.
- Возможность масштабировать сервер и клиент под конкретные задачи.

**Manager** предоставляет базовый функционал, который можно использовать для создания сложных сетевых решений. Благодаря модульности и безопасности, этот инструмент станет отличным выбором для разработки серверов и клиентов.