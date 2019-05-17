num=int(input())
l=list(map(int,input().split()))
s=l[0:num]
m=sorted(s)
print(m[-1])