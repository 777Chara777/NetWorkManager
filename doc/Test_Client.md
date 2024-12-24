```python
from Manager import IClient, Logger

class Client:
    def __init__(self) -> None:
        self.logger = Logger("Client")
        self.client = IClient("127.0.0.1", 25565)

    def connect(self):
        self.client.connect()
        self.logger.info("Client connected to server")

    def send_message(self, message: str):
        if self.client.isopen():
            self.client.sendto(message.encode())
            self.logger.info(f"Sent message: {message}")
        else:
            self.logger.error("Client is not connected")

    def close(self):
        self.client.close()
        self.logger.info("Client connection closed")
```
