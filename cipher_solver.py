"""
Cipher Solver Module
Handles various cipher decryption techniques including:
- Caesar Cipher
- Substitution Cipher
- ROT13
- Vigenère Cipher
"""

import string
from collections import Counter


class CipherSolver:
    """Solve various cipher types"""

    @staticmethod
    def caesar_cipher_brute_force(ciphertext, shift=None):
        """
        Brute force Caesar cipher by trying all 26 shifts
        
        Args:
            ciphertext (str): Encrypted text
            shift (int): Specific shift to try (1-25), or None for all
            
        Returns:
            dict: All possible decryptions with their shifts
        """
        results = {}
        
        if shift:
            shifts = [shift]
        else:
            shifts = range(1, 26)
        
        for s in shifts:
            decrypted = ""
            for char in ciphertext:
                if char.isalpha():
                    if char.isupper():
                        decrypted += chr((ord(char) - ord('A') - s) % 26 + ord('A'))
                    else:
                        decrypted += chr((ord(char) - ord('a') - s) % 26 + ord('a'))
                else:
                    decrypted += char
            results[s] = decrypted
        
        return results

    @staticmethod
    def rot13(text):
        """
        ROT13 cipher (Caesar with shift of 13)
        
        Args:
            text (str): Text to encode/decode
            
        Returns:
            str: ROT13 encoded/decoded text
        """
        result = ""
        for char in text:
            if char.isalpha():
                if char.isupper():
                    result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
                else:
                    result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            else:
                result += char
        return result

    @staticmethod
    def vigenere_cipher(text, key, decrypt=False):
        """
        Vigenère cipher encryption/decryption
        
        Args:
            text (str): Text to process
            key (str): Encryption key
            decrypt (bool): If True, decrypt; if False, encrypt
            
        Returns:
            str: Processed text
        """
        result = ""
        key = key.upper()
        key_index = 0
        
        for char in text:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - ord('A')
                if decrypt:
                    shift = -shift
                
                if char.isupper():
                    result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                
                key_index += 1
            else:
                result += char
        
        return result

    @staticmethod
    def frequency_analysis(ciphertext):
        """
        Perform frequency analysis on ciphertext
        
        Args:
            ciphertext (str): Text to analyze
            
        Returns:
            dict: Character frequencies sorted by count
        """
        # Remove non-alphabetic characters and convert to uppercase
        clean_text = ''.join(c.upper() for c in ciphertext if c.isalpha())
        
        # Count frequencies
        freq = Counter(clean_text)
        
        # Sort by frequency (descending)
        sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        
        return sorted_freq

    @staticmethod
    def atbash_cipher(text):
        """
        Atbash cipher (reverse alphabet substitution)
        A↔Z, B↔Y, etc.
        
        Args:
            text (str): Text to encode/decode
            
        Returns:
            str: Atbash encoded/decoded text
        """
        result = ""
        for char in text:
            if char.isalpha():
                if char.isupper():
                    result += chr(ord('Z') - (ord(char) - ord('A')))
                else:
                    result += chr(ord('z') - (ord(char) - ord('a')))
            else:
                result += char
        return result


if __name__ == "__main__":
    # Example usage
    solver = CipherSolver()
    
    # Caesar cipher example
    print("=== Caesar Cipher ===")
    ciphertext = "KHOOR ZRUOG"
    results = solver.caesar_cipher_brute_force(ciphertext)
    for shift, decrypted in results.items():
        print(f"Shift {shift}: {decrypted}")
    
    # ROT13 example
    print("\n=== ROT13 ===")
    text = "Hello World"
    encoded = solver.rot13(text)
    decoded = solver.rot13(encoded)
    print(f"Original: {text}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    
    # Vigenère example
    print("\n=== Vigenère Cipher ===")
    plaintext = "HELLO"
    key = "KEY"
    encrypted = solver.vigenere_cipher(plaintext, key, decrypt=False)
    decrypted = solver.vigenere_cipher(encrypted, key, decrypt=True)
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    
    # Frequency analysis
    print("\n=== Frequency Analysis ===")
    sample = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    freq = solver.frequency_analysis(sample)
    print(f"Text: {sample}")
    print(f"Frequencies: {freq}")
