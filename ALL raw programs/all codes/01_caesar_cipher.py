def caesar_encrypt(text, k):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + k) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def caesar_decrypt(text, k):
    return caesar_encrypt(text, -k)

message = input("Enter plaintext: ")
k = int(input("Enter key (1-25): ")) % 26
cipher = caesar_encrypt(message, k)
print("Ciphertext:", cipher)
print("Decrypted:", caesar_decrypt(cipher, k))
