import sys
no=int(input())
p=list(map(int,input().split()))
if no==1:
    print(*p)
    sys.exit()
g=p
for i in range(0,no): p.append(g[i])
g=[]
for i in range(0,no):
    s=0
    for j in range(i,i+(no+1)):
        s=s+p[j]
    g.append(s)
print(*g)