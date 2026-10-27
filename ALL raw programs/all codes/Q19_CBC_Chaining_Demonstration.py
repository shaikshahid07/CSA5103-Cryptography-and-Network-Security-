# Q19 - CBC Chaining Demonstration

plaintext = input("Enter plaintext: ")
iv = input("Enter initialization value: ")

if not iv:
    print("Enter an initialization value.")
else:
    previous = iv
    print("\nCBC encryption demonstration:")

    for i in range(0, len(plaintext), len(iv)):
        block = plaintext[i:i + len(iv)]
        mixed = ""

        for j in range(len(block)):
            mixed += chr(ord(block[j]) ^ ord(previous[j]))

        print("Plaintext block:", block)
        print("XOR result:", mixed)

        previous = mixed
