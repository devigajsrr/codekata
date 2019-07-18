o=int(input())
l=list(map(int,input().split()))
x=0
q=[]
for i in range(0,o):
    for j in range(i,o):
        c=sum(l[i:j+1])
        if c<x: x=c
print(x)