def create_playfair_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  
    matrix = []
    key = "".join(dict.fromkeys(key.upper().replace("J", "I") + alphabet))   #unique filter
    for i in range(0, 25, 5):
        matrix.append(list(key[i:i+5]))
    return matrix

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col

def playfair_encrypt(plaintext, key):
    matrix = create_playfair_matrix(key)
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    if len(plaintext) % 2 != 0:
        plaintext += "X"  

    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i + 1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    return ciphertext


def playfair_decrypt(plaintext, key):
    matrix = create_playfair_matrix(key)
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    if len(plaintext) % 2 != 0:
        plaintext += "X"  

    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i + 1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            ciphertext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    return ciphertext

# Example usage
plaintext = "HELLOBrother"
key = "KEYWORD"
print("Encrypted:", playfair_encrypt(plaintext, key))
print("Decrypted:", playfair_decrypt(playfair_encrypt(plaintext, key), key))