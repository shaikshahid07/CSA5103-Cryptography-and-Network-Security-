A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"; K=[[9,4],[5,7]]
def clean(s): return ''.join(c for c in s.upper() if c.isalpha())
def pairs(s):
 if len(s)%2:s+="X"
 return [s[i:i+2] for i in range(0,len(s),2)]
def inv(a): return next((x for x in range(26) if a*x%26==1),None)
def inverse(M):
 a,b=M[0];c,d=M[1];z=inv((a*d-b*c)%26)
 if z is None: raise ValueError("Key matrix not invertible modulo 26")
 return [[d*z%26,(-b)*z%26],[(-c)*z%26,a*z%26]]
def trans(q,M):
 x,y=ord(q[0])-65,ord(q[1])-65
 return ''.join(A[v%26] for v in (M[0][0]*x+M[0][1]*y,M[1][0]*x+M[1][1]*y))
p=clean("meet me at the usual place at ten rather than eight oclock");print("Key:",K);print("Plaintext:",p);c=''
for q in pairs(p):
 x,y=ord(q[0])-65,ord(q[1])-65;v=((9*x+4*y)%26,(5*x+7*y)%26);o=trans(q,K);c+=o;print(f"{q}: ({x},{y}) -> {v} -> {o}")
print("Ciphertext:",c);M=inverse(K);print("Inverse key modulo 26:",M);r=''
for q in pairs(c): o=trans(q,M);r+=o;print("Decrypt",q,"->",o)
print("Recovered plaintext:",r)
