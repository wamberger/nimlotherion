

__all__ = ['CryptoSafe']


from cryptography.fernet import Fernet


class CryptoSafe:

    __slots__ = ['key', 'safe', 'token']

    def __init__(self, data: bytes) -> None:
        self.key: bytes = Fernet.generate_key()
        self.safe: Fernet = Fernet(self.key)
        self.token: bytes = self.safe.encrypt(data)

    def decrypt(self) -> bytes:
        return self.safe.decrypt(self.token)
