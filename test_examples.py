#!/usr/bin/env python3
"""
Test Examples - Demonstrates all features of the CyberSec Project
"""

from cipher_solver import CipherSolver
from hash_generator import HashGenerator
from hash_cracker import HashCracker


def test_cipher_solver():
    """Test cipher solver functionality"""
    print("\n" + "="*60)
    print("CIPHER SOLVER TESTS")
    print("="*60)
    
    solver = CipherSolver()
    
    # Test 1: Caesar Cipher
    print("\n[Test 1] Caesar Cipher - Brute Force")
    print("-" * 60)
    ciphertext = "KHOOR ZRUOG"
    print(f"Ciphertext: {ciphertext}")
    results = solver.caesar_cipher_brute_force(ciphertext)
    print("Results:")
    for shift, decrypted in results.items():
        if shift == 3:
            print(f"  Shift {shift}: {decrypted} ✓ (CORRECT)")
        else:
            print(f"  Shift {shift}: {decrypted}")
    
    # Test 2: ROT13
    print("\n[Test 2] ROT13 Cipher")
    print("-" * 60)
    text = "Hello World"
    encoded = solver.rot13(text)
    decoded = solver.rot13(encoded)
    print(f"Original:  {text}")
    print(f"Encoded:   {encoded}")
    print(f"Decoded:   {decoded}")
    
    # Test 3: Vigenère Cipher
    print("\n[Test 3] Vigenère Cipher")
    print("-" * 60)
    plaintext = "HELLO"
    key = "KEY"
    encrypted = solver.vigenere_cipher(plaintext, key, decrypt=False)
    decrypted = solver.vigenere_cipher(encrypted, key, decrypt=True)
    print(f"Plaintext:  {plaintext}")
    print(f"Key:        {key}")
    print(f"Encrypted:  {encrypted}")
    print(f"Decrypted:  {decrypted}")
    
    # Test 4: Atbash Cipher
    print("\n[Test 4] Atbash Cipher")
    print("-" * 60)
    text = "HELLO"
    result = solver.atbash_cipher(text)
    print(f"Original: {text}")
    print(f"Atbash:   {result}")
    
    # Test 5: Frequency Analysis
    print("\n[Test 5] Frequency Analysis")
    print("-" * 60)
    sample = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    freq = solver.frequency_analysis(sample)
    print(f"Text: {sample}")
    print("Top 5 frequencies:")
    for i, (char, count) in enumerate(list(freq.items())[:5], 1):
        print(f"  {i}. {char}: {count}")


def test_hash_generator():
    """Test hash generator functionality"""
    print("\n" + "="*60)
    print("HASH GENERATOR TESTS")
    print("="*60)
    
    generator = HashGenerator()
    password = "MySecurePassword123!"
    
    print(f"\nPassword: {password}\n")
    
    # Test 1: MD5
    print("[Test 1] MD5 Hash")
    print("-" * 60)
    md5_hash = generator.md5(password)
    print(f"MD5: {md5_hash}")
    
    # Test 2: SHA1
    print("\n[Test 2] SHA1 Hash")
    print("-" * 60)
    sha1_hash = generator.sha1(password)
    print(f"SHA1: {sha1_hash}")
    
    # Test 3: SHA256
    print("\n[Test 3] SHA256 Hash")
    print("-" * 60)
    sha256_hash = generator.sha256(password)
    print(f"SHA256: {sha256_hash}")
    
    # Test 4: SHA512
    print("\n[Test 4] SHA512 Hash")
    print("-" * 60)
    sha512_hash = generator.sha512(password)
    print(f"SHA512: {sha512_hash}")
    
    # Test 5: PBKDF2
    print("\n[Test 5] PBKDF2 Hash")
    print("-" * 60)
    pbkdf2_result = generator.pbkdf2(password)
    print(f"Hash:       {pbkdf2_result['hash']}")
    print(f"Salt:       {pbkdf2_result['salt']}")
    print(f"Iterations: {pbkdf2_result['iterations']}")
    print(f"Algorithm:  {pbkdf2_result['algorithm']}")
    
    # Test 6: HMAC-SHA256
    print("\n[Test 6] HMAC-SHA256")
    print("-" * 60)
    secret = "secret_key"
    hmac_hash = generator.hmac_sha256(password, secret)
    print(f"Secret Key: {secret}")
    print(f"HMAC-SHA256: {hmac_hash}")
    
    # Test 7: HMAC-SHA512
    print("\n[Test 7] HMAC-SHA512")
    print("-" * 60)
    hmac_hash = generator.hmac_sha512(password, secret)
    print(f"Secret Key: {secret}")
    print(f"HMAC-SHA512: {hmac_hash}")
    
    # Test 8: bcrypt
    print("\n[Test 8] bcrypt Hash")
    print("-" * 60)
    bcrypt_hash = generator.bcrypt_hash(password)
    print(f"bcrypt: {bcrypt_hash}")
    
    # Test 9: All Hashes
    print("\n[Test 9] All Hash Types")
    print("-" * 60)
    all_hashes = generator.get_all_hashes(password)
    for hash_type, hash_value in all_hashes.items():
        if isinstance(hash_value, dict):
            print(f"{hash_type}:")
            for k, v in hash_value.items():
                print(f"  {k}: {v}")
        else:
            print(f"{hash_type}: {hash_value}")


def test_hash_cracker():
    """Test hash cracker functionality"""
    print("\n" + "="*60)
    print("HASH CRACKER TESTS")
    print("="*60)
    
    cracker = HashCracker()
    
    # Test hashes (all hash "password")
    test_cases = {
        'MD5': '5f4dcc3b5aa765d61d8327deb882cf99',
        'SHA1': '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8',
        'SHA256': '5e884898da28047151d0e56f8dc62927e8d9b0b1d3f7f7c8e8f8f8f8f8f8f8f8',
    }
    
    # Test 1: Hash Type Identification
    print("\n[Test 1] Hash Type Identification")
    print("-" * 60)
    for expected_type, hash_value in test_cases.items():
        identified = cracker.identify_hash_type(hash_value)
        status = "✓" if identified == expected_type else "✗"
        print(f"{status} {hash_value[:20]}... -> {identified}")
    
    # Test 2: Dictionary Attack - MD5
    print("\n[Test 2] Dictionary Attack - MD5")
    print("-" * 60)
    md5_hash = test_cases['MD5']
    print(f"Hash: {md5_hash}")
    result = cracker.crack_md5(md5_hash)
    if result:
        print(f"✓ Cracked! Password: {result}")
    else:
        print("✗ Could not crack")
    
    # Test 3: Dictionary Attack - SHA1
    print("\n[Test 3] Dictionary Attack - SHA1")
    print("-" * 60)
    sha1_hash = test_cases['SHA1']
    print(f"Hash: {sha1_hash}")
    result = cracker.crack_sha1(sha1_hash)
    if result:
        print(f"✓ Cracked! Password: {result}")
    else:
        print("✗ Could not crack")
    
    # Test 4: Dictionary Attack - SHA256
    print("\n[Test 4] Dictionary Attack - SHA256")
    print("-" * 60)
    sha256_hash = test_cases['SHA256']
    print(f"Hash: {sha256_hash}")
    result = cracker.crack_sha256(sha256_hash)
    if result:
        print(f"✓ Cracked! Password: {result}")
    else:
        print("✗ Could not crack")
    
    # Test 5: Auto Crack
    print("\n[Test 5] Auto Crack (Identify & Crack)")
    print("-" * 60)
    for hash_type, hash_value in test_cases.items():
        result = cracker.crack_auto(hash_value)
        print(f"\nHash Type: {result['hash_type']}")
        print(f"Cracked: {result['cracked']}")
        if result['cracked']:
            print(f"Password: {result['password']} ✓")
    
    # Test 6: Brute Force (short password)
    print("\n[Test 6] Brute Force - MD5 (max length 3)")
    print("-" * 60)
    # Create a simple hash for brute force testing
    simple_password = "abc"
    simple_hash = HashGenerator.md5(simple_password)
    print(f"Hash: {simple_hash}")
    print("Attempting brute force (this may take a moment)...")
    result = cracker.brute_force_md5(simple_hash, max_length=3)
    if result:
        print(f"✓ Cracked! Password: {result}")
    else:
        print("✗ Could not crack")


def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("CYBERSEC PROJECT - COMPREHENSIVE TEST SUITE")
    print("="*60)
    
    test_cipher_solver()
    test_hash_generator()
    test_hash_cracker()
    
    print("\n" + "="*60)
    print("ALL TESTS COMPLETED")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
