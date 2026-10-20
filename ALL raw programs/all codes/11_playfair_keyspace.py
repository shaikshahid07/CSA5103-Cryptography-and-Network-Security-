import math
n=math.factorial(25)
print("Playfair keyspace")
print("All arrangements: 25! =",n)
print("Approximate power of 2: 2^{:.2f}".format(math.log2(n)))
e=n//(math.factorial(5)*math.factorial(5)*2)
print("One common effective-key estimate 25!/(5!*5!*2) =",e)
print("Approximate power of 2: 2^{:.2f}".format(math.log2(e)))
print("Equivalent-key conventions can vary by textbook.")
