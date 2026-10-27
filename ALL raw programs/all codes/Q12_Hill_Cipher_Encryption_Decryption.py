# Q12 - Hill Cipher Encryption and Decryption
import math

key = [[9, 4], [5, 7]]
det = (key[0][0] * key[1][1] - key[0][1] * key[1][0]) % 26
det_inv = pow(det, -1, 26)

inv = [
    [(det_inv * key[1][1]) % 26, (-det_inv * key[0][1]) % 26],
    [(-det_inv * key[1][0]) % 26, (det_inv * key[0][0]) % 26]
]

text = input("Enter plaintext: ").lower()
text = ''.join(c for c in text if c.isalpha())

if len(text) % 2:
    text += 'x'

cipher = ""
print("\nEncryption calculations:")
for i in range(0, len(text), 2):
    a, b = ord(text[i]) - 97, ord(text[i + 1]) - 97
    x = (9 * a + 4 * b) % 26
    y = (5 * a + 7 * b) % 26
    cipher += chr(x + 97) + chr(y + 97)
    print(text[i:i+2], "->", (a, b), "->", (x, y),
          "->", cipher[-2:])

print("\nCiphertext:", cipher)
print("Determinant =", det)
print("Inverse key matrix =", inv)

plain = ""
print("\nDecryption calculations:")
for i in range(0, len(cipher), 2):
    a, b = ord(cipher[i]) - 97, ord(cipher[i + 1]) - 97
    x = (inv[0][0] * a + inv[0][1] * b) % 26
    y = (inv[1][0] * a + inv[1][1] * b) % 26
    plain += chr(x + 97) + chr(y + 97)
    print(cipher[i:i+2], "->", (a, b), "->", (x, y),
          "->", plain[-2:])

print("\nDecrypted plaintext:", plain)
