# Creating Your Own Compression

```python
from Manager.network.utils.Compression.CustomCompression import CustomCompression

compressor = CustomCompression()
data = b"This is some data that needs to be compressed."
compressed_data = compressor.compress(data)
decompressed_data = compressor.decompress(compressed_data)

print(f"Original data: {data}")
print(f"Compressed data: {compressed_data}")
print(f"Decompressed data: {decompressed_data}")
```
