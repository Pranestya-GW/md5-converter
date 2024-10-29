# hash_calculator.py

import hashlib

def calculate_md5(text):
    """Calculate the MD5 hash of a given text."""
    return hashlib.md5(text.encode()).hexdigest()
