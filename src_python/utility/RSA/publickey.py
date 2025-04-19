from dataclasses import dataclass

@dataclass
class PublicKey:
    key: tuple[int, int]
    salt: bytes
    size: int = 1024

    def encrypt(self, plaintext: str) -> str:
        e, n = self.key
        
        # Преобразование соли и текста в байты
        plaintext_bytes = self.salt + plaintext.encode('utf-8')
        
        # Шифрование всех байтов текста (с солью)
        ciphertext = [pow(byte, e, n) for byte in plaintext_bytes]

        return (' '.join( map(str, ciphertext) ))
