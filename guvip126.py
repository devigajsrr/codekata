o,k=map(int,input().split())
l=list(map(int,input().split()))
q=[]
for i in range(0,o):
    if l.count(l[i])<k: q.append(l[i])
q=sorted(q)
print(*q)