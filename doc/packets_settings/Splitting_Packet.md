```python
from Manager import splitting_package

content = "This is a long message that needs to be split into smaller packets."
packets = splitting_package(content, packet_size=20)

for packet in packets:
    print(packet)
```
