PC2=[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
def select(v):
 b=f"{v:056b}";return ''.join(b[i-1] for i in PC2)
s=input("Enter 56-bit C||D as 14 hex digits (Enter for demo): ").strip() or "0123456789ABCD";v=int(s,16)&((1<<56)-1);b=select(v)
print("C||D:",f"{v:014X}");print("PC-2 48-bit selection:",f"{int(b,2):012X}");print("PC-2 selects 24 bits from C and 24 bits from D.")
