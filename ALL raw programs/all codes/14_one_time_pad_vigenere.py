A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def clean(s):return ''.join(c for c in s.upper() if c.isalpha())
def enc(t,k):
 t=clean(t)
 if len(t)!=len(k):raise ValueError("Key length must match plaintext letter count")
 return ''.join(A[(ord(c)-65+x)%26] for c,x in zip(t,k))
def dec(t,k):return ''.join(A[(ord(c)-65-x)%26] for c,x in zip(t,k))
k=[9,0,1,7,23,15,21,14,11,11,2,8,9];c=enc("send more money",k)
print("14(a) plaintext:",clean("send more money"));print("Key stream:",k);print("Ciphertext:",c);print("Check:",dec(c,k))
t=clean("cash not needed");print("14(b) target:",t)
if len(t)!=len(c):print("Cannot use same ciphertext: ciphertext has",len(c),"letters, target has",len(t),"letters.")
else:
 nk=[(ord(x)-ord(y))%26 for x,y in zip(c,t)];print("Required key:",nk);print("Verify:",dec(c,nk))
