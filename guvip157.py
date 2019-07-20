n,o=map(int,input().split())
k=list(bin(n*o))
k=k[::-1]
print(k.index("1")+1)