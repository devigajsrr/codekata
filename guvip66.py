k=list(map(int,input().split()))
m=k[len(k)-1]
a=[i for i in input().split()]
for i in a:
    if a.count(str(i))==m:
        print(i)
        break
