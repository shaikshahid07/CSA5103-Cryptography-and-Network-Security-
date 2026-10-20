try:
 from Crypto.Cipher import DES3
 from Crypto.Random import get_random_bytes
 from Crypto.Util.Padding import pad,unpad
except ImportError:raise SystemExit("Install dependency: python -m pip install pycryptodome")
m=input("Enter plaintext: ").encode();k=DES3.adjust_key_parity(get_random_bytes(24));iv=get_random_bytes(8);c=DES3.new(k,DES3.MODE_CBC,iv);ct=c.encrypt(pad(m,8))
print("Key:",k.hex());print("IV:",iv.hex());print("CBC ciphertext:",ct.hex());d=DES3.new(k,DES3.MODE_CBC,iv);print("Recovered:",unpad(d.decrypt(ct),8).decode())
print("DES/3DES are legacy; use authenticated AES-GCM for new systems.")
