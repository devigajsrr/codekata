num=int(input())
list=list(map(int,input().split()))
s=list[0:num]
m=sorted(s)
for j in range(0,num):
    print(m[j], end=" ")