import string

plain = string.ascii_uppercase

def keyword_alphabet(keyword):
    result = []
    for ch in (keyword.upper() + plain):
        if ch in plain and ch not in result:
            result.append(ch)
    return ''.join(result)

def translate(text, source, target):
    table = str.maketrans(source + source.lower(), target + target.lower())
    return text.translate(table)

keyword = input("Enter keyword (example CIPHER): ")
cipher_alphabet = keyword_alphabet(keyword)
print("Plain alphabet :", plain)
print("Cipher alphabet:", cipher_alphabet)
message = input("Enter plaintext: ")
cipher = translate(message, plain, cipher_alphabet)
print("Ciphertext:", cipher)
print("Decrypted:", translate(cipher, cipher_alphabet, plain))
