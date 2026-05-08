"""
File Decryption Module

This module reverses the hybrid encryption process:
1. Decrypt the AES key using RSA private key.
2. Use the recovered AES key to decrypt the file.
3. Save the recovered original file.
"""

from pathlib import Path
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding


def decrypt_file(
    encrypted_file_path: Path,
    encrypted_key_path: Path,
    nonce_path: Path,
    private_key_path: Path,
    decrypted_file_path: Path
) -> None:
    """
    Decrypts a file encrypted with AES-GCM after recovering the AES key using RSA.

    Args:
        encrypted_file_path: Path to encrypted file contents.
        encrypted_key_path: Path to RSA-encrypted AES key.
        nonce_path: Path to AES-GCM nonce.
        private_key_path: Path to RSA private key.
        decrypted_file_path: Output path for recovered plaintext file.
    """

    # Load encrypted file data, encrypted AES key, and nonce.
    ciphertext = encrypted_file_path.read_bytes()
    encrypted_aes_key = encrypted_key_path.read_bytes()
    nonce = nonce_path.read_bytes()

    # Load RSA private key.
    private_key = serialization.load_pem_private_key(
        private_key_path.read_bytes(),
        password=None
    )

    # Decrypt AES key using RSA private key.
    aes_key = private_key.decrypt(
        encrypted_aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Decrypt file using recovered AES key.
    aesgcm = AESGCM(aes_key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, associated_data=None)

    # Save recovered file.
    decrypted_file_path.write_bytes(plaintext)
