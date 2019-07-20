n=list(map(str,input()))
fi=[]
s=0
for i in range(len(n)):
    if n[i]!=" " and n[i] not in fi:
        if s<n.count(n[i]):
            s=n.count(n[i])
            fi=[n[i]]
        elif s==n.count(n[i]):
            fi.append(n[i])
k="".join(fi)
print(s,end=" ")
print(k)