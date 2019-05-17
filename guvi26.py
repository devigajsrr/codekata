num=int(input())
l=list(map(int,input().split()))
s=l[0:num]
m=sorted(s)
for i in range(0,num):
    print(m[i], end=" ")