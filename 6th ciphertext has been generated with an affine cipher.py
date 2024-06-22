from sympy import mod_inverse

# Affine cipher decryption function
def affine_decrypt(ciphertext, a, b):
    decrypted = ""
    a_inv = mod_inverse(a, 26)
    for char in ciphertext:
        if char.isalpha():
            y = ord(char) - ord('A')
            x = (a_inv * (y - b)) % 26
            decrypted += chr(x + ord('A'))
        else:
            decrypted += char
    return decrypted

# Find a and b based on provided conditions
def find_keys():
    # Positions: B = 1, U = 20, E = 4, T = 19
    x1, y1 = 4, 1
    x2, y2 = 19, 20
    
    a = ((y1 - y2) * mod_inverse(x1 - x2, 26)) % 26
    b = (y1 - a * x1) % 26
    return a, b

# Example ciphertext (replace with your actual ciphertext)
ciphertext = "YOUR CIPHERTEXT HERE"

# Find the keys
a, b = find_keys()
print(f"Keys found: a = {a}, b = {b}")

# Decrypt the ciphertext
decrypted_message = affine_decrypt(ciphertext, a, b)
print("Decrypted message:", decrypted_message)
