# Q18 - DES Round Key Generation

key = input("Enter 16-digit hexadecimal key: ")

if len(key) != 16:
    print("Enter a valid 16-digit key.")
else:
    bits = bin(int(key, 16))[2:].zfill(64)
    left = bits[:28]
    right = bits[28:56]

    shifts = [1, 1, 2, 2, 2, 2, 2, 2,
              1, 2, 2, 2, 2, 2, 2, 1]

    for i, shift in enumerate(shifts, 1):
        left = left[shift:] + left[:shift]
        right = right[shift:] + right[:shift]

        print("\nRound", i)
        print("Left 28 bits =", left)
        print("Right 28 bits =", right)
