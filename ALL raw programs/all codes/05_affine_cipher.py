import math

def mod_inverse(a, m=26):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encrypt(text, a, b):
    if math.gcd(a, 26) != 1:
        raise ValueError("Invalid a: gcd(a, 26) must be 1.")
    out = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            p = ord(ch) - base
            out.append(chr(((a * p + b) % 26) + base))
        else:
            out.append(ch)
    return ''.join(out)

def decrypt(text, a, b):
    inv = mod_inverse(a % 26)
    if inv is None:
        raise ValueError("Invalid a: no modular inverse exists.")
    out = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            c = ord(ch) - base
            out.append(chr((inv * (c - b)) % 26 + base))
        else:
            out.append(ch)
    return ''.join(out)

print("Affine cipher: C = (a*p + b) mod 26")
print("b may be any integer; it is reduced modulo 26.")
print("Allowed a values:", [a for a in range(26) if math.gcd(a, 26) == 1])
text = input("Enter plaintext: ")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
cipher = encrypt(text, a, b)
print("Ciphertext:", cipher)
print("Decrypted:", decrypt(cipher, a, b))
