def make_matrix(keyword):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    chars = []
    for ch in (keyword.upper() + alphabet):
        if ch == "J":
            ch = "I"
        if ch.isalpha() and ch in alphabet and ch not in chars:
            chars.append(ch)
    return [chars[i:i + 5] for i in range(0, 25, 5)]

def prepare(text):
    text = ''.join(ch for ch in text.upper() if ch.isalpha()).replace("J", "I")
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 >= len(text):
            b = "X"
            i += 1
        elif text[i + 1] == a:
            b = "X"
            i += 1
        else:
            b = text[i + 1]
            i += 2
        pairs.append(a + b)
    return pairs

def transform(text, matrix, mode):
    pos = {matrix[r][c]: (r, c) for r in range(5) for c in range(5)}
    step = 1 if mode == "encrypt" else -1
    out = []
    for pair in prepare(text):
        a, b = pair
        r1, c1 = pos[a]
        r2, c2 = pos[b]
        if r1 == r2:
            out.extend([matrix[r1][(c1 + step) % 5], matrix[r2][(c2 + step) % 5]])
        elif c1 == c2:
            out.extend([matrix[(r1 + step) % 5][c1], matrix[(r2 + step) % 5][c2]])
        else:
            out.extend([matrix[r1][c2], matrix[r2][c1]])
    return ''.join(out)

key = input("Enter keyword: ")
message = input("Enter message: ")
matrix = make_matrix(key)
print("Playfair matrix:")
for row in matrix:
    print(' '.join(row))
cipher = transform(message, matrix, "encrypt")
print("Ciphertext:", cipher)
print("Decrypted prepared text:", transform(cipher, matrix, "decrypt"))
