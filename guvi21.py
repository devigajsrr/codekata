n,a,b=map(int,input().split())
x=0
i=0
while n>i:
    x=x+a
    a=b+a
    i=i+1
print(x)