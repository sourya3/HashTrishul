#!/usr/bin/env python3
"""
CyberSec Project - Main CLI Interface
Integrated tool for cipher solving, hash generation, and hash cracking
"""

import sys
from cipher_solver import CipherSolver
from hash_generator import HashGenerator
from hash_cracker import HashCracker


class CyberSecCLI:
    """Command-line interface for CyberSec tools"""

    def __init__(self):
        self.cipher_solver = CipherSolver()
        self.hash_generator = HashGenerator()
        self.hash_cracker = HashCracker()

    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*50)
        print("       CYBERSEC PROJECT - MAIN MENU")
        print("="*50)
        print("\n1. Cipher Solver")
        print("2. Hash Generator")
        print("3. Hash Cracker")
        print("4. Exit")
        print("\n" + "="*50)

    def cipher_menu(self):
        """Cipher solver submenu"""
        print("\n" + "="*50)
        print("       CIPHER SOLVER")
        print("="*50)
        print("\n1. Caesar Cipher (Brute Force)")
        print("2. ROT13 Cipher")
        print("3. Vigenère Cipher")
        print("4. Atbash Cipher")
        print("5. Frequency Analysis")
        print("6. Back to Main Menu")
        print("\n" + "="*50)

    def hash_generator_menu(self):
        """Hash generator submenu"""
        print("\n" + "="*50)
        print("       HASH GENERATOR")
        print("="*50)
        print("\n1. MD5 Hash")
        print("2. SHA1 Hash")
        print("3. SHA256 Hash")
        print("4. SHA512 Hash")
        print("5. PBKDF2 Hash")
        print("6. HMAC-SHA256")
        print("7. HMAC-SHA512")
        print("8. bcrypt Hash")
        print("9. Generate All Hashes")
        print("10. Back to Main Menu")
        print("\n" + "="*50)

    def hash_cracker_menu(self):
        """Hash cracker submenu"""
        print("\n" + "="*50)
        print("       HASH CRACKER")
        print("="*50)
        print("\n1. Crack MD5 (Dictionary)")
        print("2. Crack SHA1 (Dictionary)")
        print("3. Crack SHA256 (Dictionary)")
        print("4. Crack SHA512 (Dictionary)")
        print("5. Brute Force MD5")
        print("6. Brute Force SHA256")
        print("7. Auto Crack (Identify & Crack)")
        print("8. Online Lookup")
        print("9. Back to Main Menu")
        print("\n" + "="*50)

    def run_cipher_solver(self):
        """Run cipher solver operations"""
        while True:
            self.cipher_menu()
            choice = input("\nEnter your choice (1-6): ").strip()

            if choice == '1':
                ciphertext = input("Enter ciphertext: ").strip()
                results = self.cipher_solver.caesar_cipher_brute_force(ciphertext)
                print("\n--- Caesar Cipher Results ---")
                for shift, decrypted in results.items():
                    print(f"Shift {shift:2d}: {decrypted}")

            elif choice == '2':
                text = input("Enter text to encode/decode: ").strip()
                result = self.cipher_solver.rot13(text)
                print(f"\nROT13 Result: {result}")

            elif choice == '3':
                text = input("Enter text: ").strip()
                key = input("Enter key: ").strip()
                mode = input("Encrypt (e) or Decrypt (d)? ").strip().lower()
                decrypt = mode == 'd'
                result = self.cipher_solver.vigenere_cipher(text, key, decrypt)
                print(f"\nVigenère Result: {result}")

            elif choice == '4':
                text = input("Enter text: ").strip()
                result = self.cipher_solver.atbash_cipher(text)
                print(f"\nAtbash Result: {result}")

            elif choice == '5':
                text = input("Enter text to analyze: ").strip()
                freq = self.cipher_solver.frequency_analysis(text)
                print("\n--- Frequency Analysis ---")
                for char, count in freq.items():
                    percentage = (count / len([c for c in text if c.isalpha()])) * 100
                    print(f"{char}: {count} ({percentage:.2f}%)")

            elif choice == '6':
                break

            else:
                print("Invalid choice. Please try again.")

    def run_hash_generator(self):
        """Run hash generator operations"""
        while True:
            self.hash_generator_menu()
            choice = input("\nEnter your choice (1-10): ").strip()

            text = None
            if choice != '10':
                text = input("Enter text to hash: ").strip()

            if choice == '1':
                result = self.hash_generator.md5(text)
                print(f"\nMD5: {result}")

            elif choice == '2':
                result = self.hash_generator.sha1(text)
                print(f"\nSHA1: {result}")

            elif choice == '3':
                result = self.hash_generator.sha256(text)
                print(f"\nSHA256: {result}")

            elif choice == '4':
                result = self.hash_generator.sha512(text)
                print(f"\nSHA512: {result}")

            elif choice == '5':
                result = self.hash_generator.pbkdf2(text)
                print(f"\nPBKDF2:")
                print(f"  Hash: {result['hash']}")
                print(f"  Salt: {result['salt']}")
                print(f"  Iterations: {result['iterations']}")

            elif choice == '6':
                secret = input("Enter secret key: ").strip()
                result = self.hash_generator.hmac_sha256(text, secret)
                print(f"\nHMAC-SHA256: {result}")

            elif choice == '7':
                secret = input("Enter secret key: ").strip()
                result = self.hash_generator.hmac_sha512(text, secret)
                print(f"\nHMAC-SHA512: {result}")

            elif choice == '8':
                result = self.hash_generator.bcrypt_hash(text)
                print(f"\nbcrypt: {result}")

            elif choice == '9':
                results = self.hash_generator.get_all_hashes(text)
                print("\n--- All Hash Types ---")
                for hash_type, hash_value in results.items():
                    if isinstance(hash_value, dict):
                        print(f"{hash_type}:")
                        for k, v in hash_value.items():
                            print(f"  {k}: {v}")
                    else:
                        print(f"{hash_type}: {hash_value}")

            elif choice == '10':
                break

            else:
                print("Invalid choice. Please try again.")

    def run_hash_cracker(self):
        """Run hash cracker operations"""
        while True:
            self.hash_cracker_menu()
            choice = input("\nEnter your choice (1-9): ").strip()

            if choice == '1':
                hash_value = input("Enter MD5 hash: ").strip()
                result = self.hash_cracker.crack_md5(hash_value)
                if result:
                    print(f"\n✓ Cracked! Password: {result}")
                else:
                    print("\n✗ Could not crack hash with available wordlist")

            elif choice == '2':
                hash_value = input("Enter SHA1 hash: ").strip()
                result = self.hash_cracker.crack_sha1(hash_value)
                if result:
                    print(f"\n✓ Cracked! Password: {result}")
                else:
                    print("\n✗ Could not crack hash with available wordlist")

            elif choice == '3':
                hash_value = input("Enter SHA256 hash: ").strip()
                result = self.hash_cracker.crack_sha256(hash_value)
                if result:
                    print(f"\n✓ Cracked! Password: {result}")
                else:
                    print("\n✗ Could not crack hash with available wordlist")

            elif choice == '4':
                hash_value = input("Enter SHA512 hash: ").strip()
                result = self.hash_cracker.crack_sha512(hash_value)
                if result:
                    print(f"\n✓ Cracked! Password: {result}")
                else:
                    print("\n✗ Could not crack hash with available wordlist")

            elif choice == '5':
                hash_value = input("Enter MD5 hash: ").strip()
                max_len = int(input("Enter max password length (default 4): ") or "4")
                print("Brute forcing... (this may take a while)")
                result = self.hash_cracker.brute_force_md5(hash_value, max_len)
                if result:
                    print(f"\n✓ Cracked! Password: {result}")
                else:
                    print("\n✗ Could not crack hash with brute force")

            elif choice == '6':
                hash_value = input("Enter SHA256 hash: ").strip()
                max_len = int(input("Enter max password length (default 4): ") or "4")
                print("Brute forcing... (this may take a while)")
                result = self.hash_cracker.brute_force_sha256(hash_value, max_len)
                if result:
                    print(f"\n✓ Cracked! Password: {result}")
                else:
                    print("\n✗ Could not crack hash with brute force")

            elif choice == '7':
                hash_value = input("Enter hash: ").strip()
                result = self.hash_cracker.crack_auto(hash_value)
                print(f"\n--- Auto Crack Results ---")
                print(f"Hash Type: {result['hash_type']}")
                print(f"Cracked: {result['cracked']}")
                if result['cracked']:
                    print(f"Password: {result['password']}")

            elif choice == '8':
                hash_value = input("Enter hash: ").strip()
                print("Attempting online lookup...")
                result = self.hash_cracker.lookup_online(hash_value)
                if result:
                    print(f"\n✓ Found! Password: {result}")
                else:
                    print("\n✗ Not found in online database")

            elif choice == '9':
                break

            else:
                print("Invalid choice. Please try again.")

    def run(self):
        """Main application loop"""
        print("\n" + "="*50)
        print("   Welcome to CyberSec Project")
        print("="*50)

        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-4): ").strip()

            if choice == '1':
                self.run_cipher_solver()
            elif choice == '2':
                self.run_hash_generator()
            elif choice == '3':
                self.run_hash_cracker()
            elif choice == '4':
                print("\nThank you for using CyberSec Project!")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    cli = CyberSecCLI()
    cli.run()
