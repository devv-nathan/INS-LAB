# ShiftLock-128 Cipher

## Overview

**ShiftLock-128** is a custom encryption algorithm designed for **128-bit encryption strength** by combining **substitution (shift-based encryption)** and **transposition (scrambling)** techniques. It provides **strong security**, efficiency, and scalability for modern encryption needs.

## Features

- **128-bit encryption strength** ensuring high computational security.
- **Hybrid encryption approach** using substitution (shifting) and transposition (scrambling).
- **Efficient and scalable** with O(n) time and space complexity.
- **Resistant to frequency analysis, brute-force, and statistical attacks.**
- **Customizable encryption key** allowing dynamic security adjustments.

## How It Works

### **Encryption Process:**

1. Convert plaintext into numerical values (A=0, B=1, ..., Z=25).
2. Generate a **128-bit cryptographic key** to determine shift sequences.
3. Apply key-based shifts to each letter in the text.
4. Scramble the shifted text using a **key-dependent permutation function**.

### **Decryption Process:**

1. Reverse the scrambling pattern using the same key-dependent permutation.
2. Reverse the shifts using the inverse of the original shift sequence.
3. Convert numerical values back into plaintext.

## Installation & Usage

### **Requirements:**

- Python 3.x

### **Installation:**

Clone this repository:

```bash
 git clone https://github.com/devv-nathan/shiftlock-128.git
 cd shiftlock-128
```

### **Run the Cipher:**

```bash
python shiftlock_128.py
```

## Example Usage

```python
from shiftlock_128 import encrypt, decrypt

key = "YOUR_128_BIT_KEY"
plaintext = "HELLO WORLD"

ciphertext = encrypt(plaintext, key)
print("Encrypted:", ciphertext)

decrypted_text = decrypt(ciphertext, key)
print("Decrypted:", decrypted_text)
```

## Security Considerations

- The **128-bit key** ensures **high entropy** and prevents brute-force attacks.
- **Non-uniform shifting** eliminates frequency analysis weaknesses.
- **Key-dependent scrambling** prevents simple pattern recognition.

## Future Improvements

- **Multi-layer transposition for enhanced diffusion.**
- **Adaptability for different languages and character sets.**
- **Implementation in other languages (C++, Java, JavaScript).**

## License

This project is licensed under the **MIT License**. See `LICENSE` for more details.

## Contributing

Feel free to submit **issues, feature requests, or pull requests** to improve the cipher.

---

**Created by **[**devv-nathan**](https://github.com/devv-nathan)

