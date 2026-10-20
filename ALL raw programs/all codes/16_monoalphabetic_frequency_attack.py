import argparse,string
from collections import Counter
ORDER="ETAOINSHRDLCUMWFGYPBVKJXQZ";ABC=string.ascii_uppercase
def attack(t):
 f=Counter(c.upper() for c in t if c.isalpha());o=[c for c,_ in f.most_common()];o += [c for c in ABC if c not in o];m={o[i]:ORDER[i] for i in range(26)};r=''
 for c in t:
  if c.isalpha():v=m[c.upper()];r+=v if c.isupper() else v.lower()
  else:r+=c
 return r,m,f
p=argparse.ArgumentParser();p.add_argument('--top',type=int,default=10);p.add_argument('--text');a=p.parse_args();t=a.text if a.text is not None else input("Enter substitution ciphertext: ");r,m,f=attack(t)
print("Frequencies:",f.most_common());print("Candidate plaintext:",r);print("Cipher-to-plaintext guess:",m);print("Basic heuristic only; not a full solver. One candidate shown.")
