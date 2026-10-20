def vigenere(text, key, decrypt=False):
    key = ''.join(ch for ch in key.upper() if ch.isalpha())
    if not key:
        raise ValueError("Key must contain at least one letter.")
    out = []
    j = 0
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = ord(key[j % len(key)]) - ord('A')
            if decrypt:
                shift = -shift
            out.append(chr((ord(ch) - base + shift) % 26 + base))
            j += 1
        else:
            out.append(ch)
    return ''.join(out)

message = input("Enter plaintext: ")
key = input("Enter keyword: ")
cipher = vigenere(message, key)
print("Ciphertext:", cipher)
print("Decrypted:", vigenere(cipher, key, True))
