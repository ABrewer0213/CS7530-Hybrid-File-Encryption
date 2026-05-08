# IEEE Report Draft / Outline

## Title
Hybrid File Encryption System Using AES and RSA

## Author
Amonn Brewer  
Group Number: [Add Group Number Here]  
CS 7530 Spring 2026

## Abstract
This project presents a hybrid file encryption system that applies both private-key and public-key cryptography to protect sensitive files. The system uses AES-256-GCM to encrypt file contents and RSA-2048-OAEP to encrypt the AES session key. This design combines the efficiency of symmetric encryption with the key-management advantages of asymmetric encryption. The implemented Python application allows users to generate RSA keys, encrypt files, and decrypt files back to their original form. The results demonstrate that hybrid cryptography is practical for secure file storage and transfer.

## I. Introduction
Sensitive files are commonly stored and transferred through personal computers, email systems, cloud services, and organizational networks. Without encryption, these files may be exposed if a device is stolen, a transfer channel is intercepted, or unauthorized access occurs. This project addresses the problem of protecting user files through a hybrid encryption application. The goal is to apply cryptographic techniques learned in CS 7530 to a practical real-world setting.

## II. Historical Background
Encryption has been used for centuries to protect information, from classical ciphers to modern computational cryptography. Modern systems commonly use symmetric encryption for performance and asymmetric encryption for secure key exchange. AES is widely used as a symmetric encryption standard, while RSA is one of the most well-known public-key cryptosystems.

## III. Problem Statement
The problem addressed in this project is the need for a secure method to protect files during storage or transfer. Users need a way to encrypt files so that only an intended recipient with the correct private key can recover the original content.

## IV. System Design
The system uses hybrid encryption. During encryption, a random AES key is generated and used to encrypt the selected file. The AES key is then encrypted using the receiver's RSA public key. During decryption, the receiver uses the RSA private key to recover the AES key and then decrypts the file.

## V. Algorithms Used
### A. AES-256-GCM
AES is used as the private-key algorithm. AES-GCM provides confidentiality and integrity protection. A random 256-bit AES key is generated for each encryption operation.

### B. RSA-2048-OAEP
RSA is used as the public-key algorithm. The public key encrypts the AES key, and the private key decrypts it. OAEP padding with SHA-256 improves security over basic RSA encryption.

## VI. Implementation
The project was implemented in Python using the cryptography library. The program includes separate modules for key generation, encryption, and decryption. The user interacts with the program through a command-line menu.

## VII. Testing and Results
Testing should include:
- Encrypting and decrypting a text file
- Encrypting and decrypting a PDF or image file
- Confirming the decrypted file matches the original
- Recording screenshots of terminal output and file contents

Example table:

| Test File | File Type | Result |
|---|---|---|
| sample.txt | Text | Successfully encrypted and decrypted |
| image.jpg | Image | Successfully encrypted and decrypted |
| document.pdf | PDF | Successfully encrypted and decrypted |

## VIII. Challenges and Limitations
A challenge in this project was managing multiple output files, including the encrypted file, encrypted AES key, and nonce. Another limitation is that the RSA private key is not password protected in this demo version. A production system would require stronger key storage, authentication, and user access control.

## IX. Future Improvements
Future improvements could include a graphical user interface, password-protected private keys, digital signatures, cloud storage integration, and multi-user file sharing.

## X. Conclusion
This project successfully demonstrates a real-world application of private-key and public-key encryption. AES provides efficient file encryption, while RSA protects the AES key. The completed system shows how hybrid encryption can protect sensitive files during storage and transfer.

## References
[1] W. Stallings, Cryptography and Network Security: Principles and Practice. Pearson.
[2] National Institute of Standards and Technology, “Advanced Encryption Standard (AES),” FIPS PUB 197.
[3] R. Rivest, A. Shamir, and L. Adleman, “A Method for Obtaining Digital Signatures and Public-Key Cryptosystems,” Communications of the ACM.
[4] Python Cryptographic Authority, “cryptography Documentation.”
[5] National Institute of Standards and Technology, “Recommendation for Block Cipher Modes of Operation: Galois/Counter Mode.”
