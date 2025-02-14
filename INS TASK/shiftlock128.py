import random
import string

def generate_key(seed: int, length: int):
    """Generates a pseudo-random shift sequence based on a 128-bit key (seed)."""
    random.seed(seed)
    return [random.randint(1, 25) for _ in range(length)]

def encrypt(text: str, key: int):
    """Encrypts text using ShiftLock-128 Cipher."""
    shift_seq = generate_key(key, len(text))
    scrambled_indices = list(range(len(text)))
    random.seed(key)
    random.shuffle(scrambled_indices)  # Key-based scrambling
    
    encrypted_text = [''] * len(text)
    for i, char in enumerate(text):
        if char.upper() in string.ascii_uppercase:
            shifted = (ord(char.upper()) - ord('A') + shift_seq[i]) % 26
            encrypted_text[scrambled_indices[i]] = chr(ord('A') + shifted)
        else:
            encrypted_text[scrambled_indices[i]] = char
    
    return ''.join(encrypted_text)

def decrypt(text: str, key: int):
    """Decrypts text using ShiftLock-128 Cipher."""
    shift_seq = generate_key(key, len(text))
    scrambled_indices = list(range(len(text)))
    random.seed(key)
    random.shuffle(scrambled_indices)  # Reverse scrambling
    
    decrypted_text = [''] * len(text)
    for i, scrambled_index in enumerate(scrambled_indices):
        char = text[scrambled_index]
        if char.upper() in string.ascii_uppercase:
            shifted = (ord(char.upper()) - ord('A') - shift_seq[i]) % 26
            decrypted_text[i] = chr(ord('A') + shifted)
        else:
            decrypted_text[i] = char
    
    return ''.join(decrypted_text)

# Example Usage
if __name__ == "__main__":
    plaintext = input("Enter text to encrypt: ")
    key = 12345678901234567890123456789012  # Example 128-bit key (integer format)
    encrypted = encrypt(plaintext, key)
    decrypted = decrypt(encrypted, key)
    
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
