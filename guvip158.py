n,o=map(int,input().split())
k=list(bin(n*o))
print(k.index("1",k.index("1")+1,len(k))-1)