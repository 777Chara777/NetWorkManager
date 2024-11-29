from dataclasses import dataclass

@dataclass
class PrivateKey:
    key: tuple[int, int]
    salt: bytes
    size: int

    def decrypt(self, ciphertext: str) -> str:
        d, n = self.key
        
        # Расшифровка всех символов
        decrypted_bytes = [pow(char, d, n) for char in list(map(int, ciphertext.split(' '))) ]
        
        # Отделение соли от оригинального сообщения
        decrypted_text = bytes(decrypted_bytes[len(self.salt):]).decode('utf-8')
        
        return decrypted_text
        
