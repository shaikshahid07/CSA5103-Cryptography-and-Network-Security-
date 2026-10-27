# Q17 - DES Reverse Round Key Schedule

key = input("Enter 16-digit hexadecimal key: ")

if len(key) != 16:
    print("Enter a valid 16-digit key.")
else:
    bits = bin(int(key, 16))[2:].zfill(64)
    left = bits[:28]
    right = bits[28:56]

    shifts = [1, 1, 2, 2, 2, 2, 2, 2,
              1, 2, 2, 2, 2, 2, 2, 1]

    keys = []

    for shift in shifts:
        left = left[shift:] + left[:shift]
        right = right[shift:] + right[:shift]
        keys.append(left + right)

    print("Decryption round key order:")
    for i in range(15, -1, -1):
        print("K" + str(i + 1), "=", keys[i])
