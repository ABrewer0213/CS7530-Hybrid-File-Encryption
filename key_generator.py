"""
RSA Key Generator
Creates a 2048-bit RSA public/private key pair.

The public key is used to encrypt the AES key.
The private key is used to decrypt the AES key.
"""

from pathlib import Path
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


def generate_rsa_keys(private_key_path: Path, public_key_path: Path) -> None:
    """
    Generates RSA private and public keys and saves them as PEM files.

    Args:
        private_key_path: Path where the RSA private key will be saved.
        public_key_path: Path where the RSA public key will be saved.
    """

    # Generate RSA private key with 2048-bit key size.
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # Extract the public key from the private key.
    public_key = private_key.public_key()

    # Save private key without password protection for demo simplicity.
    # In a production system, this private key should be encrypted with a password.
    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Save public key.
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    private_key_path.write_bytes(private_key_bytes)
    public_key_path.write_bytes(public_key_bytes)
