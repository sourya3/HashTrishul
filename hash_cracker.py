"""
Hash Cracker Module
Crack hashes using:
- Dictionary attacks
- Brute force
- Rainbow tables (online lookup)
- Common password lists
"""

import hashlib
import itertools
import string
import requests
from pathlib import Path


class HashCracker:
    """Crack various hash types"""

    def __init__(self, wordlist_path=None):
        """
        Initialize hash cracker
        
        Args:
            wordlist_path (str): Path to custom wordlist file
        """
        self.wordlist_path = wordlist_path
        self.common_passwords = [
            'password', '123456', '12345678', 'qwerty', 'abc123',
            'monkey', '1234567', 'letmein', 'trustno1', 'dragon',
            'baseball', '111111', 'iloveyou', 'master', 'sunshine',
            'ashley', 'bailey', 'passw0rd', 'shadow', '123123',
            '654321', 'superman', 'qazwsx', 'michael', 'football'
        ]

    def load_wordlist(self):
        """
        Load wordlist from file
        
        Returns:
            list: Words from wordlist
        """
        if not self.wordlist_path or not Path(self.wordlist_path).exists():
            return self.common_passwords
        
        try:
            with open(self.wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                return [word.strip() for word in f.readlines()]
        except Exception as e:
            print(f"Error loading wordlist: {e}")
            return self.common_passwords

    def crack_md5(self, hash_value, wordlist=None):
        """
        Crack MD5 hash using dictionary attack
        
        Args:
            hash_value (str): MD5 hash to crack
            wordlist (list): List of words to try
            
        Returns:
            str: Cracked password or None
        """
        if wordlist is None:
            wordlist = self.load_wordlist()
        
        for word in wordlist:
            if hashlib.md5(word.encode()).hexdigest() == hash_value:
                return word
        
        return None

    def crack_sha1(self, hash_value, wordlist=None):
        """
        Crack SHA1 hash using dictionary attack
        
        Args:
            hash_value (str): SHA1 hash to crack
            wordlist (list): List of words to try
            
        Returns:
            str: Cracked password or None
        """
        if wordlist is None:
            wordlist = self.load_wordlist()
        
        for word in wordlist:
            if hashlib.sha1(word.encode()).hexdigest() == hash_value:
                return word
        
        return None

    def crack_sha256(self, hash_value, wordlist=None):
        """
        Crack SHA256 hash using dictionary attack
        
        Args:
            hash_value (str): SHA256 hash to crack
            wordlist (list): List of words to try
            
        Returns:
            str: Cracked password or None
        """
        if wordlist is None:
            wordlist = self.load_wordlist()
        
        for word in wordlist:
            if hashlib.sha256(word.encode()).hexdigest() == hash_value:
                return word
        
        return None

    def crack_sha512(self, hash_value, wordlist=None):
        """
        Crack SHA512 hash using dictionary attack
        
        Args:
            hash_value (str): SHA512 hash to crack
            wordlist (list): List of words to try
            
        Returns:
            str: Cracked password or None
        """
        if wordlist is None:
            wordlist = self.load_wordlist()
        
        for word in wordlist:
            if hashlib.sha512(word.encode()).hexdigest() == hash_value:
                return word
        
        return None

    def brute_force_md5(self, hash_value, max_length=4, charset=None):
        """
        Brute force MD5 hash
        
        Args:
            hash_value (str): MD5 hash to crack
            max_length (int): Maximum password length to try
            charset (str): Character set to use
            
        Returns:
            str: Cracked password or None
        """
        if charset is None:
            charset = string.ascii_lowercase + string.digits
        
        for length in range(1, max_length + 1):
            for attempt in itertools.product(charset, repeat=length):
                password = ''.join(attempt)
                if hashlib.md5(password.encode()).hexdigest() == hash_value:
                    return password
        
        return None

    def brute_force_sha256(self, hash_value, max_length=4, charset=None):
        """
        Brute force SHA256 hash
        
        Args:
            hash_value (str): SHA256 hash to crack
            max_length (int): Maximum password length to try
            charset (str): Character set to use
            
        Returns:
            str: Cracked password or None
        """
        if charset is None:
            charset = string.ascii_lowercase + string.digits
        
        for length in range(1, max_length + 1):
            for attempt in itertools.product(charset, repeat=length):
                password = ''.join(attempt)
                if hashlib.sha256(password.encode()).hexdigest() == hash_value:
                    return password
        
        return None

    def lookup_online(self, hash_value, hash_type='md5'):
        """
        Lookup hash on online rainbow table (using md5.gromweb.com)
        
        Args:
            hash_value (str): Hash to lookup
            hash_type (str): Type of hash (md5, sha1, sha256)
            
        Returns:
            str: Cracked password or None
        """
        try:
            # Using md5.gromweb.com API
            url = f"https://md5.gromweb.com/?md5={hash_value}"
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 0:
                    return data.get('password')
            
            return None
        except Exception as e:
            print(f"Online lookup failed: {e}")
            return None

    def identify_hash_type(self, hash_value):
        """
        Identify hash type by length
        
        Args:
            hash_value (str): Hash to identify
            
        Returns:
            str: Identified hash type
        """
        hash_len = len(hash_value)
        
        hash_types = {
            32: 'MD5',
            40: 'SHA1',
            56: 'SHA224',
            64: 'SHA256',
            96: 'SHA384',
            128: 'SHA512'
        }
        
        return hash_types.get(hash_len, 'Unknown')

    def crack_auto(self, hash_value, wordlist=None):
        """
        Automatically identify hash type and attempt to crack
        
        Args:
            hash_value (str): Hash to crack
            wordlist (list): List of words to try
            
        Returns:
            dict: Results with hash type and cracked password
        """
        hash_type = self.identify_hash_type(hash_value)
        
        result = {
            'hash': hash_value,
            'hash_type': hash_type,
            'cracked': False,
            'password': None
        }
        
        if hash_type == 'MD5':
            password = self.crack_md5(hash_value, wordlist)
        elif hash_type == 'SHA1':
            password = self.crack_sha1(hash_value, wordlist)
        elif hash_type == 'SHA256':
            password = self.crack_sha256(hash_value, wordlist)
        elif hash_type == 'SHA512':
            password = self.crack_sha512(hash_value, wordlist)
        else:
            password = None
        
        if password:
            result['cracked'] = True
            result['password'] = password
        
        return result


if __name__ == "__main__":
    # Example usage
    cracker = HashCracker()
    
    # Test hashes
    test_hashes = {
        'md5': '5f4dcc3b5aa765d61d8327deb882cf99',  # 'password'
        'sha1': '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8',  # 'password'
        'sha256': '5e884898da28047151d0e56f8dc62927e8d9b0b1d3f7f7c8e8f8f8f8f8f8f8f8',  # 'password'
    }
    
    print("=== Hash Cracking Examples ===\n")
    
    for hash_type, hash_value in test_hashes.items():
        print(f"Attempting to crack {hash_type.upper()}: {hash_value}")
        result = cracker.crack_auto(hash_value)
        print(f"Result: {result}\n")
