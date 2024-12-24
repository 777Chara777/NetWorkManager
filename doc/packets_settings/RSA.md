```python
from Manager.utility.RSA.rsa import RSA

rsa = RSA(1024)
public_key, private_key = rsa.generate_keys()

message = "This is a secret message."
encrypted_message = rsa.encrypt(message, public_key)
decrypted_message = rsa.decrypt(encrypted_message, private_key)

print(f"Original message: {message}")
print(f"Encrypted message: {encrypted_message}")
print(f"Decrypted message: {decrypted_message}")
```
