# README

## Manager: Network Tool

### Description

**Manager** is a powerful tool designed for network interactions. It provides developers with the means to create both servers and clients using a unified package-based approach. **Manager** is not a ready-made server or client itself but serves as a flexible foundation for their development.

The core idea is to create standardized packages that can be used for data exchange between clients and servers, as well as handling events.

---

## Download

1. Clone the repository:

    ```sh
    git clone https://github.com/777Chara777/NetWorkManager.git
    ```

2. Go to the project directory:

    ```sh
    cd Manager
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt 
    ```

---

## Key Features

1. **Packet Registration**  
    Manager allows for the registration of packages and the events associated with them, which are processed during interaction.

2. **RSA Support**  
    Traffic encryption is performed using RSA, ensuring the security of transmitted data.

3. **Modular Architecture**  
    - The system allows for adding and processing custom packages.  
    - Convenient tool for separating tasks between event handlers and packages.

4. **Flexibility and Scalability**  
    Manager provides base classes and methods that can be adapted for applications of any scale.

---

## Example Usage

- [ ] Creating a [**Server**](./doc/Test_Server.md)

- [ ] Creating a [**Client**](./doc/Test_Client.md)

- [X] Creating a [**Packet**](./doc/packets_settings/Creating_Packet.md)

- [ ] Register a [**Packet**](./doc/packets_settings/Registering_Packet.md)

- [ ] Creating a [**Compression methode**](./doc/packets_settings/Compression_Packet.md)

- See all [**./examples/**](./doc/)

---

## Main Modules

- **RegisterPacket**  
  Registering custom packets and associated events.

- **ListeningEvents**  
  Handling events related to packages.

- **CustomPacket**  
  Base class for creating custom packets.

- **RSA**  
  Utility for encrypting data.

- **Logger**  
  Convenient logging system for tracking server and client activity. See [examples](./doc/Logger.md)

---

## Extensibility

- Easily add your own packet types.  
- Simple integration of custom event handlers.  
- Ability to scale the server and client for specific needs.

**Manager** provides the foundational functionality needed to create complex network solutions. With its modularity and security, this tool is an excellent choice for developing servers and clients.

## Problemssss

- You can report a problem [here](https://github.com/777Chara777/NetWorkManager/issues/1)
