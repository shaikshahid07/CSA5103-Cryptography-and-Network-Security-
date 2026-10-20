import string

plain = string.ascii_uppercase
cipher_alphabet = input("Enter 26-letter substitution alphabet: ").strip().upper()
if len(cipher_alphabet) != 26 or set(cipher_alphabet) != set(plain):
    raise SystemExit("Invalid key: enter each A-Z letter exactly once.")

def encrypt(text):
    table = str.maketrans(plain + plain.lower(),
                          cipher_alphabet + cipher_alphabet.lower())
    return text.translate(table)

def decrypt(text):
    table = str.maketrans(cipher_alphabet + cipher_alphabet.lower(),
                          plain + plain.lower())
    return text.translate(table)

message = input("Enter plaintext: ")
cipher = encrypt(message)
print("Ciphertext:", cipher)
print("Decrypted:", decrypt(cipher))
