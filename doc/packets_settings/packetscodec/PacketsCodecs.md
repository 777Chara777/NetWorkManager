# Creating Your Own Codec

This document provides a detailed guide on how to create and use custom codecs in the system.

## Introduction

A codec is a class that provides methods for encoding and decoding data. In this system, codecs are used to transform data into a byte format for transmission and then back into the original format upon receipt.

## Example: Creating a Custom Codec

Below is an example of creating a simple `Integer` codec.

### Step 1: Define the Codec Class

First, create a new Python file for your codec. In this example, we'll create a file named `Integer.py` and inherit the [Codec](/Manager/network/utils/Packet/typings/Codec.py) class

```python
from Manager.network.utils.Packet.typings.Codec import Codec

class Integer(Codec):

    @staticmethod
    def encode(value: int) -> bytes:
        return value.to_bytes(4, 'big')

    @staticmethod
    def decode(buffer: bytes, offset: int) -> int:
        value = int.from_bytes(buffer[offset:offset+4], 'big')
        return value, offset + 4
```

### Step 2: Implement the Codec Methods

In the Integer class, we implement the encode and decode methods. The encode method converts an integer to a 4-byte big-endian format, and the decode method converts a 4-byte big-endian format back to an integer.

### Step 3: Use the Codec

Now you can use your custom codec in your code. Here's an example of how to use the Integer codec.

```python
from CustomCodecs.MyInteger import Integer

# Encoding an integer
encoded = Integer.encode(12345)
print(f"Encoded: {encoded}")

# Decoding the integer
decoded, _ = Integer.decode(encoded, 0)
print(f"Decoded: {decoded}")
```

### Summary

Creating a custom codec involves the following steps:

- [Step 1](#step-1-define-the-codec-class) Define the codec class by inheriting from the Codec abstract base class.
- [Step 2](#step-2-implement-the-codec-methods) Implement the encode and decode methods.
- [Step 3](#step-3-use-the-codec) Use the codec in your code.

To see the structure, follow the interface: [Codec](/Manager/network/utils/Packet/typings/Codec.py)

### Brief Example of Codec Structure

```python
class Codec(ABC):

    @staticmethod
    @abstractmethod
    def encode(value: str) -> bytes:
        """Method for serializing a value"""

    @staticmethod
    @abstractmethod
    def decode(buffer: bytes, offset: int) -> Any:
        """Method for deserializing a value"""
```
