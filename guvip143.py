o=int(input())
k=list(map(int,input().split()))
l=list(map(int,input().split()))
for i in range(0,o):
    for j in range(i+1,o):
        if l[i]>l[j]:
            t=k[i]
            k[i]=k[j]
            k[j]=t
print(*k)