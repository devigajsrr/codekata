n,m=map(int,input().split())
d=0
a=n*m
x=max(n,m)
for i in range(1,x+1):
    if n%i==0 and m%i==0:
        d=i
print(int(a/d))
