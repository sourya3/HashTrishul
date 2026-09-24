# CyberSec Project

A comprehensive Python-based cybersecurity toolkit for cipher solving, hash generation, and hash cracking.

## Features

### 1. Cipher Solver
- **Caesar Cipher**: Brute force all 26 possible shifts
- **ROT13**: Encode/decode ROT13 cipher
- **Vigenère Cipher**: Encrypt/decrypt with key-based cipher
- **Atbash Cipher**: Reverse alphabet substitution
- **Frequency Analysis**: Analyze character frequencies in text

### 2. Hash Generator
- **MD5**: Generate MD5 hashes (legacy, not recommended for passwords)
- **SHA1**: Generate SHA1 hashes (legacy, not recommended for passwords)
- **SHA256**: Generate SHA256 hashes
- **SHA512**: Generate SHA512 hashes
- **PBKDF2**: Password-based key derivation with salt and iterations
- **HMAC-SHA256**: Hash-based message authentication code
- **HMAC-SHA512**: Hash-based message authentication code
- **bcrypt**: Secure password hashing with salt rounds

### 3. Hash Cracker
- **Dictionary Attack**: Crack hashes using wordlist
- **Brute Force**: Exhaustive search with configurable character set
- **Auto Crack**: Automatically identify hash type and attempt cracking
- **Online Lookup**: Query online rainbow tables (md5.gromweb.com)

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Setup

```bash
# Clone or navigate to project directory
cd ~/CyberSecProject

# Install dependencies
pip install -r requirements.txt

# Optional: Install bcrypt for bcrypt support
pip install bcrypt
```

## Usage

### Interactive CLI

```bash
python main.py
```

This launches an interactive menu-driven interface with options for:
1. Cipher Solver
2. Hash Generator
3. Hash Cracker
4. Exit

### Programmatic Usage

#### Cipher Solver

```python
from cipher_solver import CipherSolver

solver = CipherSolver()

# Caesar cipher brute force
results = solver.caesar_cipher_brute_force("KHOOR ZRUOG")
for shift, decrypted in results.items():
    print(f"Shift {shift}: {decrypted}")

# ROT13
encoded = solver.rot13("Hello World")
decoded = solver.rot13(encoded)

# Vigenère cipher
encrypted = solver.vigenere_cipher("HELLO", "KEY", decrypt=False)
decrypted = solver.vigenere_cipher(encrypted, "KEY", decrypt=True)

# Frequency analysis
freq = solver.frequency_analysis("THEQUICKBROWNFOX")
```

#### Hash Generator

```python
from hash_generator import HashGenerator

generator = HashGenerator()

# Generate various hashes
md5_hash = generator.md5("password")
sha256_hash = generator.sha256("password")
sha512_hash = generator.sha512("password")

# PBKDF2 with salt
pbkdf2_result = generator.pbkdf2("password")
# Returns: {'hash': '...', 'salt': '...', 'iterations': 100000, 'algorithm': 'sha256'}

# HMAC
hmac_hash = generator.hmac_sha256("message", "secret_key")

# bcrypt
bcrypt_hash = generator.bcrypt_hash("password")
is_valid = generator.bcrypt_verify("password", bcrypt_hash)

# All hashes at once
all_hashes = generator.get_all_hashes("password")
```

#### Hash Cracker

```python
from hash_cracker import HashCracker

cracker = HashCracker()

# Dictionary attack
password = cracker.crack_md5("5f4dcc3b5aa765d61d8327deb882cf99")

# Brute force
password = cracker.brute_force_md5("5f4dcc3b5aa765d61d8327deb882cf99", max_length=4)

# Auto crack (identify hash type and crack)
result = cracker.crack_auto("5f4dcc3b5aa765d61d8327deb882cf99")
# Returns: {'hash': '...', 'hash_type': 'MD5', 'cracked': True, 'password': 'password'}

# Online lookup
password = cracker.lookup_online("5f4dcc3b5aa765d61d8327deb882cf99")

# Identify hash type
hash_type = cracker.identify_hash_type("5f4dcc3b5aa765d61d8327deb882cf99")
```

## Hash Type Identification

The tool automatically identifies hash types by length:
- 32 characters: MD5
- 40 characters: SHA1
- 56 characters: SHA224
- 64 characters: SHA256
- 96 characters: SHA384
- 128 characters: SHA512

## Security Notes

⚠️ **Important Security Considerations:**

1. **MD5 & SHA1**: These are cryptographically broken and should NOT be used for password hashing
2. **SHA256/SHA512**: Suitable for general hashing but not ideal for passwords without salt
3. **PBKDF2**: Good for password hashing with configurable iterations
4. **bcrypt**: Recommended for password hashing (uses salt and adaptive cost)
5. **Dictionary Attacks**: Effective against weak passwords; use strong, unique passwords
6. **Brute Force**: Computationally expensive; practical only for short passwords

## Example Workflows

### Crack a Password Hash

```bash
python main.py
# Select option 3 (Hash Cracker)
# Select option 7 (Auto Crack)
# Enter hash: 5f4dcc3b5aa765d61d8327deb882cf99
# Result: Password found!
```

### Generate Secure Password Hash

```bash
python main.py
# Select option 2 (Hash Generator)
# Select option 8 (bcrypt Hash)
# Enter text: MySecurePassword123!
# Result: $2b$12$... (bcrypt hash)
```

### Solve Caesar Cipher

```bash
python main.py
# Select option 1 (Cipher Solver)
# Select option 1 (Caesar Cipher)
# Enter ciphertext: KHOOR ZRUOG
# Result: All 26 shifts displayed (Shift 3: HELLO WORLD)
```

## Project Structure

```
CyberSecProject/
├── main.py                 # Interactive CLI interface
├── cipher_solver.py        # Cipher solving utilities
├── hash_generator.py       # Hash generation utilities
├── hash_cracker.py         # Hash cracking utilities
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Testing

Run individual modules to test functionality:

```bash
# Test cipher solver
python cipher_solver.py

# Test hash generator
python hash_generator.py

# Test hash cracker
python hash_cracker.py
```

## Limitations

1. **Dictionary Attack**: Limited by wordlist size
2. **Brute Force**: Exponentially slower with password length
3. **Online Lookup**: Requires internet connection; limited to common hashes
4. **bcrypt Verification**: Requires bcrypt library installation

## Future Enhancements

- [ ] Support for more cipher types (Playfair, Enigma simulation)
- [ ] GPU-accelerated brute force
- [ ] Custom wordlist support
- [ ] Rainbow table generation
- [ ] Multi-threaded cracking
- [ ] Support for salted hash cracking
- [ ] Web interface

## Legal Disclaimer

This tool is for educational and authorized security testing purposes only. Unauthorized access to computer systems is illegal. Always obtain proper authorization before testing security systems.

## License

MIT License - Feel free to use and modify for educational purposes.

## Author

Created as a comprehensive cybersecurity learning project.

## References

- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [Cryptography.io Documentation](https://cryptography.io/)
- [Python hashlib Documentation](https://docs.python.org/3/library/hashlib.html)
# HashTrishul
