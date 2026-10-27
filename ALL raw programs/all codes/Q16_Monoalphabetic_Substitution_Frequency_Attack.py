# Q16 - Monoalphabetic Substitution Frequency Attack

cipher = input("Enter ciphertext: ").lower()
top = int(input("Enter number of top plaintexts: "))

english = "etaoinshrdlcumwfgypbvkjxqz"
counts = {}

for ch in cipher:
    if ch.isalpha():
        counts[ch] = counts.get(ch, 0) + 1

ranked = sorted(counts, key=counts.get, reverse=True)
letters = "abcdefghijklmnopqrstuvwxyz"
mapping = {}

for i in range(len(ranked)):
    mapping[ranked[i]] = english[i]

plain = ""
for ch in cipher:
    plain += mapping.get(ch, ch)

print("\nPossible plaintexts:")
for i in range(min(top, 5)):
    candidate = list(plain)
    for j in range(i):
        candidate = [
            english[(english.index(c) + 1) % 26]
            if c in english else c for c in candidate
        ]
    print(i + 1, ":", "".join(candidate))
