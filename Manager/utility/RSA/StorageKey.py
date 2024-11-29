from .privatekey import PrivateKey
from .publickey import PublicKey

class StorageKey:
    def __init__(self, pu: PublicKey, pr: PrivateKey) -> None:
        self.public = pu
        self.private = pr

    def encrypt(self, context: str):
        return self.public.encrypt(context)
    
    def decrypt(self, context: str):
        return self.private.decrypt(context)