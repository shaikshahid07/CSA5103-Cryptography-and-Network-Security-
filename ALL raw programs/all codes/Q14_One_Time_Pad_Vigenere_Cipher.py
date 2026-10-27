# Q14 - One-Time Pad Vigenere Cipher
def clean(text):
    return ''.join(c.lower() for c in text if c.isalpha())

def encrypt(text, key):
    return ''.join(chr((ord(ch) - 97 + k) % 26 + 97)
                   for ch, k in zip(text, key))

plaintext = clean(input("Enter plaintext: "))
key = list(map(int, input("Enter key stream: ").split()))

if len(plaintext) != len(key) or any(k < 0 or k > 25 for k in key):
    print("Error: key length must match plaintext and values must be 0-25.")
else:
    ciphertext = encrypt(plaintext, key)
    print("Ciphertext =", ciphertext)

    target = clean(input("Enter target plaintext for part (b): "))

    if len(target) != len(ciphertext):
        print("Error: target plaintext must have the same number of letters.")
    else:
        new_key = [
            (ord(c) - 97 - (ord(p) - 97)) % 26
            for c, p in zip(ciphertext, target)
        ]

        recovered = ''.join(
            chr((ord(c) - 97 - k) % 26 + 97)
            for c, k in zip(ciphertext, new_key)
        )

        print("New key stream =", *new_key)
        print("Decrypted plaintext =", recovered)
