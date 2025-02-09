# Playfair-Cipher
The Playfair Cipher is a digraph substitution cipher, meaning it encrypts pairs of letters (digraphs) instead of single letters.The Playfair Cipher is case-insensitive.

## Working
1. Key Matrix:
    - A 5x5 matrix is created using a keyword. The letters of the keyword are filled first, and the remaining letters of the alphabet (excluding "J," which is combined with "I") are filled in order.
2. Plaintext:
    - The plaintext is split into pairs of two letters (digraphs). If a pair has the same letter, an "X" is inserted between them. If the plaintext has an odd number of letters, an "X" is added at the end.
3. Encryption:
    - If both letters are in the same row, each letter is replaced by the letter to its right.
    - If both letters are in the same column, each letter is replaced by the letter below it.
    - If the letters form a rectangle, each letter is replaced by the letter in its own row but in the column of the other letter.
4. Decryption:
    - The same rules are applied in reverse to decrypt the ciphertext.


## References
[Playfair Cipher(Click me for better understanding)](https://medium.com/@sabikchamp/playfair-cipher-984f8e289ab9])

