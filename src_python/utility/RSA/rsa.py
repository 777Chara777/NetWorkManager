import random
import os
from sympy import isprime

from .privatekey import PrivateKey
from .publickey import PublicKey

__all__ = (
    "RSA",
    "encrypt",
    "decrypt",
)

class RSA:
    def __init__(self, key_size=1024):
        self.key_size = key_size

        # Генерация случайной соли длиной 16 байт
        self.salt: bytes = os.urandom(16)

    def generate_keys(self) -> tuple[PublicKey, PrivateKey]:
        # Генерация двух простых чисел p и q
        p = self.generate_prime()
        q = self.generate_prime()

        # Вычисление модуля n
        n = p * q

        # Вычисление функции Эйлера phi(n)
        phi = (p - 1) * (q - 1)

        # Выбор e - целого числа, которое взаимно просто с phi(n)
        e = self.find_coprime(phi)

        # Вычисление закрытого ключа d
        d = self.modinv(e, phi)

        # Публичный ключ (e, n) и приватный ключ (d, n)
        return PublicKey((e, n), self.salt, self.key_size), PrivateKey((d, n), self.salt, self.key_size)

    def generate_prime(self):
        while True:
            prime_candidate = random.getrandbits(self.key_size // 2)
            if isprime(prime_candidate):
                return prime_candidate

    def find_coprime(self, phi):
        e = 2
        while self.gcd(e, phi) != 1:
            e += 1
        return e

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def modinv(self, a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1



