def caesar(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            ciphertext += chr((ord(char) + key - shift ) % 26 + shift)
        else:
            ciphertext += char
            return ciphertext

def dcaesar(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            ciphertext += chr((ord(char) - key - shift ) % 26 + shift)
        else:
            ciphertext += char
            return ciphertext


str=str(input("enter string:"))
key = int(input("enter key:"))
encrypted = caesar(str, key)
print(f"Encrypted text: {encrypted}")
decrypted = dcaesar(encrypted, key)
print(f"Decrypted text: {decrypted}")
