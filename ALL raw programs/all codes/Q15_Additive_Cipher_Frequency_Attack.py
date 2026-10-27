# Q15 - Letter Frequency Attack on Additive Cipher
import string

frequency = [
    0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020,
    0.061, 0.070, 0.002, 0.008, 0.040, 0.024, 0.067,
    0.075, 0.019, 0.001, 0.060, 0.063, 0.091, 0.028,
    0.010, 0.024, 0.002, 0.020, 0.001
]

ciphertext = input("Enter ciphertext: ").lower()
top_n = int(input("Enter number of top plaintexts: "))

letters = ''.join(c for c in ciphertext if c in string.ascii_lowercase)

if not letters or top_n < 1:
    print("Enter valid ciphertext and a positive number.")
else:
    results = []

    for shift in range(26):
        plaintext = ''.join(
            chr((ord(c) - 97 - shift) % 26 + 97)
            if c.isalpha() else c
            for c in ciphertext
        )

        counts = [letters.count(chr(97 + i)) for i in range(26)]
        decrypted = ''.join(
            chr((ord(c) - 97 - shift) % 26 + 97)
            for c in letters
        )

        total = len(decrypted)
        score = 0

        for i in range(26):
            observed = decrypted.count(chr(97 + i))
            expected = total * frequency[i]

            if expected > 0:
                score += (observed - expected) ** 2 / expected

        results.append((score, shift, plaintext))

    results.sort()

    print("\nTop possible plaintexts:")
    for i, (score, shift, plaintext) in enumerate(
        results[:min(top_n, 26)], 1
    ):
        print(i, "| Shift:", shift, "| Score:", round(score, 2),
              "| Plaintext:", plaintext)
