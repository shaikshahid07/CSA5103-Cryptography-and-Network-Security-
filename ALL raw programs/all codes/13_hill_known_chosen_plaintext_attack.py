MOD=26
def mul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%MOD for j in range(len(B[0]))] for i in range(len(A))]
key=[[3,3],[2,5]];P=[[1,0],[0,1]];C=mul(key,P)
print("Hill known/chosen plaintext attack")
print("Chosen plaintext matrix P:",P);print("Demo key K:",key);print("Observed C=K*P mod 26:",C);print("Since P is identity, recovered K=C.")
print("General formula: K=C*inverse(P) mod 26 when P is invertible.")
