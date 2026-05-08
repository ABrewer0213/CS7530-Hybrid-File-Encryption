"""
File Encryption Module
This module performs hybrid encryption:
1. Generate a random AES-256 key.
2. Encrypt the selected file using AES-GCM.
3. Encrypt the AES key using the recipient's RSA public key.
4. Save the encrypted file, encrypted AES key, and nonce.
"""

import os
from pathlib import Path
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding


def encrypt_file(
    input_file_path: Path,
    public_key_path: Path,
    encrypted_file_path: Path,
    encrypted_key_path: Path,
    nonce_path: Path
) -> None:
    """
    Encrypts a file using AES-256-GCM and encrypts the AES key using RSA-OAEP.

    Args:
        input_file_path: Path to the original file.
        public_key_path: Path to the RSA public key.
        encrypted_file_path: Output path for encrypted file contents.
        encrypted_key_path: Output path for RSA-encrypted AES key.
        nonce_path: Output path for AES-GCM nonce.
    """

    # Read original file data.
    plaintext = input_file_path.read_bytes()

    # Generate a 256-bit AES key.
    aes_key = AESGCM.generate_key(bit_length=256)

    # AES-GCM requires a unique nonce for each encryption.
    # 12 bytes is the recommended nonce size for GCM.
    nonce = os.urandom(12)

    # Encrypt file data using AES-GCM.
    aesgcm = AESGCM(aes_key)
    ciphertext = aesgcm.encrypt(nonce, plaintext, associated_data=None)

    # Load RSA public key.
    public_key = serialization.load_pem_public_key(
        public_key_path.read_bytes()
    )

    # Encrypt AES key with RSA public key using OAEP padding.
    encrypted_aes_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save outputs.
    encrypted_file_path.write_bytes(ciphertext)
    encrypted_key_path.write_bytes(encrypted_aes_key)
    nonce_path.write_bytes(nonce)
