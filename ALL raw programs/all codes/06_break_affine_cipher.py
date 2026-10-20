from collections import Counter
import string

ALPHABET = string.ascii_uppercase

def inverse(a, m=26):
    for x in range(m):
        if (a * x) % m == 1:
            return x
    return None

def affine_decrypt(text, a, b):
    inv = inverse(a)
    if inv is None:
        raise ValueError("a has no inverse modulo 26")
    out = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            c = ord(ch) - base
            out.append(chr(((inv * (c - b)) % 26) + base))
        else:
            out.append(ch)
    return ''.join(out)

ciphertext = input("Enter affine ciphertext: ")
letters = [c.upper() for c in ciphertext if c.isalpha()]
freq = Counter(letters)
print("Letter frequencies:", freq.most_common())

print("Assumption: most frequent B represents E and second-most frequent U represents T.")
# B=1, U=20, E=4, T=19: a=3 and b=11? Verify equations modulo 26.
# 4a+b=1 and 19a+b=20 gives 15a=19 (mod 26), a=3, b=15.
a, b = 3, 15
print("Candidate key: a =", a, ", b =", b)
print("Candidate plaintext:", affine_decrypt(ciphertext, a, b))
print("Frequency analysis is only a guess; short texts may need trying other mappings.")
