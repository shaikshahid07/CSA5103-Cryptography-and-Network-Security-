# Q20 - ECB and CBC Error Propagation

blocks = int(input("Enter number of ciphertext blocks: "))
error_block = int(input("Enter block containing the error: "))

if blocks < 1 or error_block < 1 or error_block > blocks:
    print("Invalid block number.")
else:
    print("\nECB mode:")
    print("Affected plaintext block:", error_block)

    print("\nCBC mode:")
    print("Affected plaintext blocks:", error_block, "and",
          error_block + 1 if error_block < blocks else "none after it")

    print("\nA ciphertext error affects the same ECB plaintext block.")
    print("In CBC, it corrupts the corresponding block and flips")
    print("the matching bit in the following plaintext block.")
