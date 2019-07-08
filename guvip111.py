o,k=map(int,input().split())
l=list(map(int,input().split()))
f=l[0:o]
s=l[o:len(l)]
p=[]
for i in range(max(k,o)):
    if f[i] in s:
        p.append(f[i])
p=sorted(p)
print(*p)