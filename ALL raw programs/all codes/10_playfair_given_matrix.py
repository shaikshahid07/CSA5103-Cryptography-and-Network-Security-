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

def encrypt(text, matrix):
    pos = {matrix[r][c]: (r, c) for r in range(5) for c in range(5)}
    out = []
    for pair in prepare(text):
        a, b = pair
        r1, c1 = pos[a]
        r2, c2 = pos[b]
        if r1 == r2:
            out.extend([matrix[r1][(c1 + 1) % 5], matrix[r2][(c2 + 1) % 5]])
        elif c1 == c2:
            out.extend([matrix[(r1 + 1) % 5][c1], matrix[(r2 + 1) % 5][c2]])
        else:
            out.extend([matrix[r1][c2], matrix[r2][c1]])
    return ''.join(out)

matrix = [
    list("MFHIK"),
    list("UNOPQ"),
    list("ZVWXY"),
    list("ELARG"),
    list("DSTBC")
]
message = "Must see you over Cadogan West. Coming at once."
print("Playfair matrix:")
for row in matrix:
    print(' '.join(row))
print("Message:", message)
print("Prepared pairs:", ' '.join(prepare(message)))
print("Ciphertext:", encrypt(message, matrix))
