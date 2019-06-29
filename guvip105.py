n=int(input())
o=list(map(int,input().split()))
g=sorted(o)
w=[]
for i in range(0,n): w.append(o.index(g[i])+1)
print(*w)