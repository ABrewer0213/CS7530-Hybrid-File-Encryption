"""
CS 7530 Spring 2026 Project
Hybrid File Encryption System Using AES and RSA

Author: Amonn Brewer
Group Number: [Add Group Number Here]

Description:
This program demonstrates hybrid cryptography by using:
1. AES-256-GCM as the private-key/symmetric encryption algorithm
2. RSA-2048-OAEP as the public-key/asymmetric encryption algorithm

AES encrypts the file contents.
RSA encrypts the AES key so it can be safely shared with the receiver.
"""

from pathlib import Path
from key_generator import generate_rsa_keys
from encrypt_file import encrypt_file
from decrypt_file import decrypt_file


def print_menu():
    print("\n========================================")
    print(" CS 7530 Hybrid File Encryption System")
    print("========================================")
    print("1. Generate RSA public/private keys")
    print("2. Encrypt a file")
    print("3. Decrypt a file")
    print("4. Exit")


def main():
    project_dir = Path(__file__).parent
    keys_dir = project_dir / "keys"
    output_dir = project_dir / "output"

    keys_dir.mkdir(exist_ok=True)
    output_dir.mkdir(exist_ok=True)

    public_key_path = keys_dir / "public_key.pem"
    private_key_path = keys_dir / "private_key.pem"

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            generate_rsa_keys(
                private_key_path=private_key_path,
                public_key_path=public_key_path
            )
            print(f"\nRSA keys generated successfully.")
            print(f"Private key: {private_key_path}")
            print(f"Public key:  {public_key_path}")

        elif choice == "2":
            file_path = input("Enter the path of the file to encrypt: ").strip()
            input_path = Path(file_path)

            if not input_path.exists():
                print("Error: File not found.")
                continue

            if not public_key_path.exists():
                print("Error: Public key not found. Generate keys first.")
                continue

            encrypted_file_path = output_dir / f"{input_path.name}.encrypted"
            encrypted_key_path = output_dir / f"{input_path.name}.aes_key.encrypted"
            nonce_path = output_dir / f"{input_path.name}.nonce"

            encrypt_file(
                input_file_path=input_path,
                public_key_path=public_key_path,
                encrypted_file_path=encrypted_file_path,
                encrypted_key_path=encrypted_key_path,
                nonce_path=nonce_path
            )

            print("\nFile encrypted successfully.")
            print(f"Encrypted file: {encrypted_file_path}")
            print(f"Encrypted AES key: {encrypted_key_path}")
            print(f"AES-GCM nonce: {nonce_path}")

        elif choice == "3":
            encrypted_file = input("Enter encrypted file path: ").strip()
            encrypted_key = input("Enter encrypted AES key path: ").strip()
            nonce_file = input("Enter nonce file path: ").strip()
            output_name = input("Enter output decrypted file name: ").strip()

            encrypted_file_path = Path(encrypted_file)
            encrypted_key_path = Path(encrypted_key)
            nonce_path = Path(nonce_file)
            decrypted_file_path = output_dir / output_name

            required_files = [
                encrypted_file_path,
                encrypted_key_path,
                nonce_path,
                private_key_path
            ]

            if not all(path.exists() for path in required_files):
                print("Error: One or more required files are missing.")
                continue

            decrypt_file(
                encrypted_file_path=encrypted_file_path,
                encrypted_key_path=encrypted_key_path,
                nonce_path=nonce_path,
                private_key_path=private_key_path,
                decrypted_file_path=decrypted_file_path
            )

            print("\nFile decrypted successfully.")
            print(f"Decrypted file: {decrypted_file_path}")

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
