# CS 7530 Hybrid File Encryption System

**Author:** Amonn Brewer  
**Course:** CS 7530 Spring 2026  
**Project Title:** Hybrid File Encryption System Using AES and RSA  

## Project Description

This project is a real-world cryptography application that protects files using hybrid encryption. The system uses AES-256-GCM as the private-key encryption algorithm and RSA-2048-OAEP as the public-key encryption algorithm.

AES is used to encrypt the actual file contents because it is fast and efficient for large data. RSA is used to encrypt the AES key because public-key encryption allows the AES key to be protected without directly sharing it.

## Algorithms Used

### Private-Key Encryption
- AES-256-GCM

### Public-Key Encryption
- RSA-2048 with OAEP padding and SHA-256

## Folder Structure

```text
CS7530_Hybrid_File_Encryption_Project/
│
├── main.py
├── key_generator.py
├── encrypt_file.py
├── decrypt_file.py
├── requirements.txt
├── README.md
├── test_files/
│   └── sample.txt
├── output/
├── keys/
├── screenshots/
└── docs/
```

## Installation

Install Python 3.10 or newer.

Install the required library:

```bash
pip install -r requirements.txt
```

## How to Run

From the project folder, run:

```bash
python main.py
```

## Demo Steps

### Step 1: Generate RSA Keys

Choose option:

```text
1. Generate RSA public/private keys
```

This creates:

```text
keys/private_key.pem
keys/public_key.pem
```

### Step 2: Encrypt a File

Choose option:

```text
2. Encrypt a file
```

For the file path, enter:

```text
test_files/sample.txt
```

The program creates:

```text
output/sample.txt.encrypted
output/sample.txt.aes_key.encrypted
output/sample.txt.nonce
```

### Step 3: Decrypt the File

Choose option:

```text
3. Decrypt a file
```

Enter:

```text
Encrypted file path: output/sample.txt.encrypted
Encrypted AES key path: output/sample.txt.aes_key.encrypted
Nonce file path: output/sample.txt.nonce
Output decrypted file name: decrypted_sample.txt
```

The program creates:

```text
output/decrypted_sample.txt
```

## Expected Result

The decrypted file should contain the same text as the original `sample.txt`.
