no=int(input())
p=list(map(int,input().split()))
p=p[::-1]
g=[]
for i in range(0,no):
    s=p[i]
    for j in range(i+1,no):
        s=s+p[j]
    g.append(s)
print(*g)
