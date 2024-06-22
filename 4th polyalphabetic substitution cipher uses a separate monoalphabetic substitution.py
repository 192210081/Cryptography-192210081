def generate_playfair_square(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = ''.join(sorted(set(key.upper().replace('J', 'I')), key=lambda x: key.index(x)))
    square = [c for c in key if c in alphabet]
    for c in alphabet:
        if c not in square:
            square.append(c)
    return [square[i:i+5] for i in range(0, 25, 5)]

def preprocess_text(text):
    text = text.upper().replace('J', 'I')
    processed = ""
    i = 0
    while i < len(text):
        processed += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            processed += 'X'
        elif i + 1 < len(text):
            processed += text[i + 1]
            i += 1
        i += 1
    if len(processed) % 2 != 0:
        processed += 'X'
    return processed

def find_position(char, square):
    for i, row in enumerate(square):
        if char in row:
            return i, row.index(char)
    return None, None

def playfair_encrypt(text, key):
    square = generate_playfair_square(key)
    text = preprocess_text(text)
    encrypted_text = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        row1, col1 = find_position(a, square)
        row2, col2 = find_position(b, square)
        if row1 == row2:
            encrypted_text += square[row1][(col1 + 1) % 5] + square[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += square[(row1 + 1) % 5][col1] + square[(row2 + 1) % 5][col2]
        else:
            encrypted_text += square[row1][col2] + square[row2][col1]
    return encrypted_text

def playfair_decrypt(text, key):
    square = generate_playfair_square(key)
    decrypted_text = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        row1, col1 = find_position(a, square)
        row2, col2 = find_position(b, square)
        if row1 == row2:
            decrypted_text += square[row1][(col1 - 1) % 5] + square[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += square[(row1 - 1) % 5][col1] + square[(row2 - 1) % 5][col2]
        else:
            decrypted_text += square[row1][col1] + square[row2][col2]
    return decrypted_text

# Example usage
key = "PLAYFAIREXAMPLE"
plaintext = "HIDETHEGOLDINTHETREESTUMP"
ciphertext = playfair_encrypt(plaintext, key)
decryptedtext = playfair_decrypt(ciphertext, key)

print("Key: ", key)
print("Plaintext: ", plaintext)
print("Ciphertext: ", ciphertext)
print("Decrypted text: ", decryptedtext)
