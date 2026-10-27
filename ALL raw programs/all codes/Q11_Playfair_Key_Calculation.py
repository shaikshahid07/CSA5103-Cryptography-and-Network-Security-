# Q11 - Playfair Cipher Key Calculation
import math

n = int(input("Enter number of letters in key matrix: "))

possible = math.factorial(n)
unique = possible // (n * n)

print("Possible keys =", possible)
print("Approximate power of 2 =", round(math.log2(possible), 2))
print("Effectively unique keys =", unique)
print("Unique keys approximately = 2^", round(math.log2(unique), 2))
