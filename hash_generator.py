"""
Hash Generator Module
Create various hash types for passwords and data:
- MD5
- SHA1
- SHA256
- SHA512
- PBKDF2
- bcrypt (if available)
"""

import hashlib
import hmac
import os
from binascii import hexlify


class HashGenerator:
    """Generate various hash types"""

    @staticmethod
    def md5(text):
        """
        Generate MD5 hash (NOT recommended for passwords)
        
        Args:
            text (str): Text to hash
            
        Returns:
            str: MD5 hash in hexadecimal
        """
        return hashlib.md5(text.encode()).hexdigest()

    @staticmethod
    def sha1(text):
        """
        Generate SHA1 hash (NOT recommended for passwords)
        
        Args:
            text (str): Text to hash
            
        Returns:
            str: SHA1 hash in hexadecimal
        """
        return hashlib.sha1(text.encode()).hexdigest()

    @staticmethod
    def sha256(text):
        """
        Generate SHA256 hash
        
        Args:
            text (str): Text to hash
            
        Returns:
            str: SHA256 hash in hexadecimal
        """
        return hashlib.sha256(text.encode()).hexdigest()

    @staticmethod
    def sha512(text):
        """
        Generate SHA512 hash
        
        Args:
            text (str): Text to hash
            
        Returns:
            str: SHA512 hash in hexadecimal
        """
        return hashlib.sha512(text.encode()).hexdigest()

    @staticmethod
    def pbkdf2(text, salt=None, iterations=100000, hash_name='sha256'):
        """
        Generate PBKDF2 hash (password-based key derivation)
        
        Args:
            text (str): Text to hash
            salt (str): Salt value (generated if None)
            iterations (int): Number of iterations
            hash_name (str): Hash algorithm (sha256, sha512, etc.)
            
        Returns:
            dict: Contains hash, salt, and iterations
        """
        if salt is None:
            salt = os.urandom(32)
        elif isinstance(salt, str):
            salt = salt.encode()
        
        key = hashlib.pbkdf2_hmac(
            hash_name,
            text.encode(),
            salt,
            iterations
        )
        
        return {
            'hash': hexlify(key).decode(),
            'salt': hexlify(salt).decode(),
            'iterations': iterations,
            'algorithm': hash_name
        }

    @staticmethod
    def hmac_sha256(text, secret_key):
        """
        Generate HMAC-SHA256 hash
        
        Args:
            text (str): Text to hash
            secret_key (str): Secret key for HMAC
            
        Returns:
            str: HMAC-SHA256 hash in hexadecimal
        """
        return hmac.new(
            secret_key.encode(),
            text.encode(),
            hashlib.sha256
        ).hexdigest()

    @staticmethod
    def hmac_sha512(text, secret_key):
        """
        Generate HMAC-SHA512 hash
        
        Args:
            text (str): Text to hash
            secret_key (str): Secret key for HMAC
            
        Returns:
            str: HMAC-SHA512 hash in hexadecimal
        """
        return hmac.new(
            secret_key.encode(),
            text.encode(),
            hashlib.sha512
        ).hexdigest()

    @staticmethod
    def bcrypt_hash(text):
        """
        Generate bcrypt hash (requires bcrypt library)
        
        Args:
            text (str): Text to hash
            
        Returns:
            str: bcrypt hash
        """
        try:
            import bcrypt
            salt = bcrypt.gensalt(rounds=12)
            return bcrypt.hashpw(text.encode(), salt).decode()
        except ImportError:
            return "bcrypt library not installed. Install with: pip install bcrypt"

    @staticmethod
    def bcrypt_verify(text, hashed):
        """
        Verify bcrypt hash
        
        Args:
            text (str): Plain text to verify
            hashed (str): bcrypt hash to verify against
            
        Returns:
            bool: True if matches, False otherwise
        """
        try:
            import bcrypt
            return bcrypt.checkpw(text.encode(), hashed.encode())
        except ImportError:
            return False

    @staticmethod
    def get_all_hashes(text):
        """
        Generate all available hash types for a given text
        
        Args:
            text (str): Text to hash
            
        Returns:
            dict: All hash types
        """
        return {
            'md5': HashGenerator.md5(text),
            'sha1': HashGenerator.sha1(text),
            'sha256': HashGenerator.sha256(text),
            'sha512': HashGenerator.sha512(text),
            'pbkdf2': HashGenerator.pbkdf2(text),
            'hmac_sha256': HashGenerator.hmac_sha256(text, 'secret_key'),
            'hmac_sha512': HashGenerator.hmac_sha512(text, 'secret_key'),
        }


if __name__ == "__main__":
    # Example usage
    generator = HashGenerator()
    
    password = "MySecurePassword123!"
    
    print("=== Hash Generation Examples ===\n")
    
    print(f"Original Password: {password}\n")
    
    print(f"MD5: {generator.md5(password)}")
    print(f"SHA1: {generator.sha1(password)}")
    print(f"SHA256: {generator.sha256(password)}")
    print(f"SHA512: {generator.sha512(password)}\n")
    
    pbkdf2_result = generator.pbkdf2(password)
    print(f"PBKDF2:")
    print(f"  Hash: {pbkdf2_result['hash']}")
    print(f"  Salt: {pbkdf2_result['salt']}")
    print(f"  Iterations: {pbkdf2_result['iterations']}\n")
    
    print(f"HMAC-SHA256: {generator.hmac_sha256(password, 'secret_key')}")
    print(f"HMAC-SHA512: {generator.hmac_sha512(password, 'secret_key')}\n")
    
    print(f"bcrypt: {generator.bcrypt_hash(password)}")
