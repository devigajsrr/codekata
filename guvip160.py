n,o=map(int,input().split())
k=list(bin(n|o))
print(k.count("1"))