n=int(input())
p=list(map(int,input().split()))
for i in range(1,100000):
    s=0
    for j in range(0,n):
        if i%p[j]==0: s=s+1
    if s==n:
        print(i)
        break