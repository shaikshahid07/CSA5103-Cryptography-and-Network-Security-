SHIFTS=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1];MASK=(1<<28)-1
def left(x,n):return ((x<<n)|(x>>(28-n)))&MASK
def keys(c,d):
 r=[]
 for s in SHIFTS:c,d=left(c,s),left(d,s);r.append((c<<28)|d)
 return r
c=int(input("Enter 28-bit C0 hex (e.g. 0123456): "),16)&MASK;d=int(input("Enter 28-bit D0 hex (e.g. 0654321): "),16)&MASK;k=keys(c,d)
print("DES decryption applies round subkeys in reverse: K16 ... K1.");print("Intermediate C||D states only; PC-2 is not applied.")
for i,v in enumerate(k,1):print(f"K{i:02}: {v:014X}")
print("Reverse order:")
for i,v in enumerate(reversed(k),1):print(f"Round {i:02}: {v:014X}")
