# Logger Module Documentation

## Overview

The `Logger` module provides a simple and flexible logging mechanism for your Python applications. It allows you to log messages with different severity levels and customize the output format and destination.

## Installation

To use the [`Logger`](/Manager/utility/Logger/logger.py) module, simply import it into your project:

```python
from Manager.utility.Logger.logger import Logger
```

## Usage

### Creating a Logger Instance

To create a logger instance, initialize the `Logger` class with a name:

```python
logger = Logger("ExampleLogger")
```

### Logging Messages

You can log messages with different severity levels using the following methods:

```python
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warm("This is a warning message")
logger.error("This is an error message")
```

### Customizing the Logger

You can customize the logger's output format, weight, and output file.

#### Setting the Message Format

To set a custom message format, use the `set_format` class method:

```python
Logger.set_format("[{time}:{level}] ({name}:{func}:{line}): {message}")
```

#### Setting the Print Weight

To set the minimum weight for messages to be printed to the console, use the `set_wight` class method:

```python
Logger.set_wight(1)
```

#### Setting the Output File

To set a file where log messages will be written, use the `set_outprint` class method:

```python
Logger.set_outprint("logfile.txt")
```

### Resetting the Logger Configuration

To reset the logger configuration to its default values, use the `reset` class method:

```python
Logger.reset()
```

## Example

Here is a complete example demonstrating the usage of the `Logger` module:

```python
from Manager.utility.Logger.logger import Logger

logger = Logger("ExampleLogger")
logger.info("This is an info message")
logger.debug("This is a debug message")
logger.warm("This is a warning message")
logger.error("This is an error message")

Logger.set_format("[{time}:{level}] ({name}:{func}:{line}): {message}")
Logger.set_wight(1)
Logger.set_outprint("logfile.txt")

logger.info("This message will be logged to the file")
```

### output

```sh
> python test.py
[02:04:09:INFO] (ExampleLogger:<module>:4): This is an info message
[02:04:09:DEBUG] (ExampleLogger:<module>:5): This is a debug message
[02:04:09:WARNUNG] (ExampleLogger:<module>:6): This is a warning message
[02:04:09:ERROR] (ExampleLogger:<module>:7): This is an error message
> ls
logfile.txt  test.py

> cat logfile.txt
[02:04:09:INFO] (ExampleLogger:<module>:13): This message will be logged to the file
```
