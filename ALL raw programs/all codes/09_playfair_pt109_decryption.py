def make_matrix(keyword):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    chars = []
    for ch in (keyword.upper() + alphabet):
        if ch == "J":
            ch = "I"
        if ch in alphabet and ch not in chars:
            chars.append(ch)
    return [chars[i:i + 5] for i in range(0, 25, 5)]

def playfair_decrypt(ciphertext, keyword):
    matrix = make_matrix(keyword)
    pos = {matrix[r][c]: (r, c) for r in range(5) for c in range(5)}
    text = ''.join(ch for ch in ciphertext.upper() if ch.isalpha()).replace("J", "I")
    if len(text) % 2:
        raise ValueError("Ciphertext must contain an even number of letters.")
    out = []
    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        r1, c1 = pos[a]
        r2, c2 = pos[b]
        if r1 == r2:
            out.extend([matrix[r1][(c1 - 1) % 5], matrix[r2][(c2 - 1) % 5]])
        elif c1 == c2:
            out.extend([matrix[(r1 - 1) % 5][c1], matrix[(r2 - 1) % 5][c2]])
        else:
            out.extend([matrix[r1][c2], matrix[r2][c1]])
    return ''.join(out)

ciphertext = """KXJEY UREBE ZWEHE WRYTU HEYFS
KREHE GOYFI WTTTU OLKSY CAJPO
BOTEI ZONTX BYBNT GONEY CUZWR
GDSON SXBOU YWRHE BAAHY USEDQ"""

print("Enter the exact Playfair keyword used by your course/textbook.")
keyword = input("Keyword: ")
print("Matrix:")
for row in make_matrix(keyword):
    print(' '.join(row))
print("Decrypted prepared text:", playfair_decrypt(ciphertext, keyword))
print("Note: the original key is required; different keywords produce different plaintext.")
