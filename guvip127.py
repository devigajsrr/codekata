o=list(map(str,input().split()))
k=str(input())
o.pop(o.index(k))
print(*o)
