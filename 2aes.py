#AES encryption in Python using the cryptography library, using two keys:
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def encrypt(plaintext: bytes, key1: bytes, key2: bytes) -> bytes:
    # Pad the plaintext to be a multiple of 16 bytes (the block size for AES)
    padder = algorithms.Padding(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    # Generate two AES cipher objects with the given keys and concatenate them
    key1_cipher = Cipher(algorithms.AES(key1), modes.ECB(), backend=default_backend())
    key2_cipher = Cipher(algorithms.AES(key2), modes.ECB(), backend=default_backend())
    double_cipher = key1_cipher.encryptor() + key2_cipher.decryptor()

    # Encrypt the padded plaintext using the concatenated cipher object
    ciphertext = double_cipher.update(padded_plaintext) + double_cipher.finalize()
    return ciphertext
