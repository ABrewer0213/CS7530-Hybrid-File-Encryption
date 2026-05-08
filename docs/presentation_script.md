# Presentation Script

## Slide 1: Title
Hello, my name is Amonn Brewer, and my project is titled Hybrid File Encryption System Using AES and RSA. This project demonstrates how private-key and public-key cryptography can be combined to protect sensitive files.

## Slide 2: Problem Definition
The problem I am addressing is the need to securely store and transfer files. Many files contain sensitive information, and if those files are sent through an insecure channel or accessed by an unauthorized person, the data can be exposed.

## Slide 3: Project Goal
The goal of this project is to build a Python application that encrypts a file using AES and protects the AES key using RSA. This creates a hybrid encryption system.

## Slide 4: Background
AES is a symmetric encryption algorithm, meaning the same key is used to encrypt and decrypt the data. RSA is an asymmetric encryption algorithm, meaning it uses a public key and private key pair.

## Slide 5: Why Hybrid Encryption?
AES is fast and efficient for encrypting large files. RSA is slower, but it is useful for protecting small pieces of data such as encryption keys. By combining them, the system gains the benefits of both methods.

## Slide 6: System Design
The system has three main parts: key generation, file encryption, and file decryption. During encryption, the program creates an AES key, encrypts the file, then encrypts the AES key with the RSA public key.

## Slide 7: Decryption Process
During decryption, the RSA private key decrypts the AES key. The recovered AES key is then used to decrypt the file and restore the original content.

## Slide 8: Implementation
The project was written in Python using the cryptography library. The code is organized into separate files for the main menu, RSA key generation, encryption, and decryption.

## Slide 9: Demo
For the demo, I will generate RSA keys, encrypt a sample file, show the encrypted output, then decrypt it and verify that the recovered file matches the original.

## Slide 10: Results
The system successfully encrypted and decrypted the test file. The encrypted file was unreadable without the private key and AES key, while the decrypted file matched the original file.

## Slide 11: Challenges and Limitations
One challenge was managing the encrypted file, encrypted AES key, and nonce as separate outputs. A limitation is that the demo private key is not password protected. In a real production system, stronger key storage would be required.

## Slide 12: Future Work
Future improvements could include a graphical interface, password-protected keys, digital signatures, cloud storage integration, and support for multiple users.

## Slide 13: Conclusion
This project demonstrates how AES and RSA can be used together in a practical cybersecurity application. The system satisfies the project requirement by applying one private-key encryption algorithm and one public-key encryption algorithm to a real-world file protection problem.

## Slide 14: References
List at least five references including AES documentation, RSA paper, Python cryptography documentation, and a textbook reference.
