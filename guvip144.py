o=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(1,o):
    if l[i]%l[i-1]==0:
        k.append(l[i])
print(*k)
