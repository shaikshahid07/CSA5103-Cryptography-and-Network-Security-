import argparse,string
F={'E':12.70,'T':9.06,'A':8.17,'O':7.51,'I':6.97,'N':6.75,'S':6.33,'H':6.09,'R':5.99,'D':4.25,'L':4.03,'C':2.78,'U':2.76,'M':2.41,'W':2.36,'F':2.23,'G':2.02,'Y':1.97,'P':1.93,'B':1.29,'V':.98,'K':.77,'J':.15,'X':.15,'Q':.10,'Z':.07}
def dec(s,k):return ''.join(chr((ord(c.upper())-65-k)%26+(65 if c.isupper() else 97)) if c.isalpha() else c for c in s)
def score(s):
 q=[c.upper() for c in s if c.isalpha()]
 if not q:return -1e9
 n=len(q);return -sum(((q.count(c)*100/n-F[c])**2)/(F[c]+.1) for c in string.ascii_uppercase)
p=argparse.ArgumentParser();p.add_argument('--top',type=int,default=10);p.add_argument('--text');a=p.parse_args();t=a.text if a.text is not None else input("Enter additive-cipher ciphertext: ")
for i,(sc,k,s) in enumerate(sorted(((score(dec(t,k)),k,dec(t,k)) for k in range(26)),reverse=True)[:max(1,a.top)],1):print(f"{i}. shift={k}, score={sc:.2f}: {s}")
