# Q13 - Hill Cipher Known Plaintext Attack
import math

plain = input("Enter known plaintext (at least 4 letters): ").lower()
cipher = input("Enter corresponding ciphertext: ").lower()

plain = ''.join(c for c in plain if c.isalpha())
cipher = ''.join(c for c in cipher if c.isalpha())

if len(plain) < 4 or len(cipher) < 4:
    print("Enter at least 4 letters in both texts.")
elif len(plain) != len(cipher) or len(plain) % 2:
    print("Plaintext and ciphertext lengths must be equal and even.")
else:
    p = [ord(c) - 97 for c in plain[:4]]
    c = [ord(ch) - 97 for ch in cipher[:4]]

    det = (p[0] * p[3] - p[2] * p[1]) % 26

    if math.gcd(det, 26) != 1:
        print("Attack failed: choose different plaintext pairs.")
    else:
        d_inv = pow(det, -1, 26)

        inv = [
            [(d_inv * p[3]) % 26, (-d_inv * p[2]) % 26],
            [(-d_inv * p[1]) % 26, (d_inv * p[0]) % 26]
        ]

        key = [
            [(c[0] * inv[0][0] + c[2] * inv[1][0]) % 26,
             (c[0] * inv[0][1] + c[2] * inv[1][1]) % 26],
            [(c[1] * inv[0][0] + c[3] * inv[1][0]) % 26,
             (c[1] * inv[0][1] + c[3] * inv[1][1]) % 26]
        ]

        print("Plaintext matrix =", [[p[0], p[2]], [p[1], p[3]]])
        print("Ciphertext matrix =", [[c[0], c[2]], [c[1], c[3]]])
        print("Recovered key matrix:")
        for row in key:
            print(row)

        result = ""
        for i in range(0, len(plain), 2):
            a, b = ord(plain[i]) - 97, ord(plain[i+1]) - 97
            x = (key[0][0] * a + key[0][1] * b) % 26
            y = (key[1][0] * a + key[1][1] * b) % 26
            result += chr(x + 97) + chr(y + 97)

        print("Verified ciphertext =", result)
        print("Actual ciphertext   =", cipher)
        print("Key verification =", result == cipher)
