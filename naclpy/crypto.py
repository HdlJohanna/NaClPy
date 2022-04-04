from cryptography.fernet import Fernet

def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)

def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)

def make_key() -> bytes:
    """
    The make_key function returns a random key.
    
    :return: The sha256 hash of the input string.
        """
    
    return Fernet.generate_key()


def load_key(filename:str) -> bytes:
    return open(filename,"rb").read()
