from typing import Any

import Manager.network.utils.Packet.PacketCodecs as PacketCodecs
from Manager.network.utils.Packet.CustomPacket import CustomPacket

from Manager.network.utils.exceptions.PacketDecodingError import PacketDecodingError


class PacketCodec:
    """
---

## `PacketCodec` Class

The `PacketCodec` class is responsible for encoding and decoding data to facilitate its transmission between a client and a server. It transforms custom objects (like packets) into byte sequences for network transmission (encoding) and reconstructs those objects from byte sequences upon receiving data (decoding).

### Constructor

```python
def __init__(self, mainclass, *codec_fields: tuple["PacketCodecs", Any]) -> None:
```

- **`mainclass`**: This is a reference to the class that will be encoded and decoded.
- **`codec_fields`**: A list of tuples where each tuple contains a codec and a getter function. These fields define how the object’s attributes will be encoded and decoded.

### Methods

#### `encode`

```python
def encode(self, cls: "CustomPacket") -> bytes:
```

This method encodes an object of type `CustomPacket` into a byte sequence for transmission.

- **Parameters**:
  - `cls`: The object to encode, usually a packet or custom class.
  
- **Returns**: 
  - A `bytes` object representing the encoded data.
  
- **Functionality**: 
  - Iterates over the `codec_fields`, retrieves the values of the object using the provided getter functions, and encodes each field using the corresponding codec.
  - The result is a sequence of bytes ready to be transmitted over the network.

#### `decode`

```python
def decode(self, buffer: bytes, offset: int) -> list[Any]:
```

This method decodes a byte sequence into a list of values, corresponding to the fields of the original object.

- **Parameters**:
  - `buffer`: A `bytes` object that contains the encoded data.
  - `offset`: The starting position for decoding within the byte buffer.
  
- **Returns**:
  - A list of decoded values, representing the fields of the original object.
  
- **Functionality**:
  - Iterates through the `codec_fields`, using each codec to extract values from the byte buffer.
  - The decoded values are returned in the order in which they were encoded.

### Example Usage

```python
class AuthPacket(CustomPacket):

    def __init__(self, password: str, name: str) -> None:
        self.password = password
        self.name = name

    def getPassword(self) -> str:
        return self.password
    
    def getNick(self) -> str:
        return self.name

    @staticmethod
    def getId() -> str:
        return "AuthPacket"

    @staticmethod
    def getCodec() -> PacketCodec:
        return PacketCodec(AuthPacket, (
            PacketCodecs.Integer16, AuthPacket.getPassword
        ), (
            PacketCodecs.String, AuthPacket.getNick,
        ) )
```

### Key Points:
- **Encoding**: Converts an object into a byte sequence suitable for transmission over the network.
- **Decoding**: Converts a byte sequence back into the corresponding fields of an object.
- **Flexibility**: The `PacketCodec` can handle any object, provided the appropriate codecs for each field are specified.

    """
    def __init__(self, mainclass: "CustomPacket", *codec_fields: tuple["PacketCodecs", Any]) -> None:
        self._codec_fields = codec_fields
        # Изменить! создать базу с иминами и ссылками на пакеты и записывать название пакета(id) 
        self.mainclass = mainclass

    def __str__(self):
        return f"< Codec {self.mainclass.__name__} >"

    # @staticmethod
    def encode(self, cls: "CustomPacket") -> bytes:
        """This method encodes an object of type `CustomPacket` into a byte sequence for transmission.

        Parameters:
            cls: The object to encode, usually a packet or custom class.

        Returns:
            bytes: object representing the encoded data.

        Functionality: 
            Iterates over the `codec_fields`, retrieves the values of the object using the provided getter functions, and encodes each field using the corresponding codec.
            The result is a sequence of bytes ready to be transmitted over the network.
        """
    
        payload = b''
        
        if len(self._codec_fields) == 0: return payload

        for codec, getter in self._codec_fields:
            if not callable(getter):
                raise ValueError(f"Getter {getter} is not callable")
            if not hasattr(codec, "encode") or not callable(codec.encode):
                raise TypeError(f"Codec {codec} does not have a callable `encode` method")
            
            value = getter(cls)
            payload += codec.encode(value)

        return payload

    # @staticmethod
    def decode(self, buffer: bytes, offset: int) -> list[Any]:
        """This method decodes a byte sequence into a list of values, corresponding to the fields of the original object.

        Parameters:
            buffer: A `bytes` object that contains the encoded data.
            offset: The starting position for decoding within the byte buffer.
        
        Returns:
            list[Any]: A list of decoded values, representing the fields of the original object.
        
        Functionality:
            Iterates through the `codec_fields`, using each codec to extract values from the byte buffer.
            The decoded values are returned in the order in which they were encoded.
        """

        if not isinstance(buffer, bytes):
            raise TypeError(f"Expected `buffer` to be of type `bytes`, got {type(buffer).__name__}")
        if not isinstance(offset, int):
            raise TypeError(f"Expected `offset` to be of type `int`, got {type(offset).__name__}")


        values = []

        if len(self._codec_fields) == 0: return values

        try:
            for codec, _ in self._codec_fields:
                if not hasattr(codec, "decode") or not callable(codec.decode):
                    raise TypeError(f"Codec {codec} does not have a callable `decode` method")

                value, offset = codec.decode(buffer, offset)
                values.append(value)
        except Exception as e:
            raise PacketDecodingError(f"Error decoding packet: {e}")
        return values