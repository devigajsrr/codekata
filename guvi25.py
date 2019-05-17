num=int(input())
l=list(map(int,input().split()))
s=l[0:num]
m=sorted(s)
x=int(num/2)
print(m[x])
