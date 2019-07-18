p=int(input())
a=[int(x) for x in input().split()]
c=a[0]
for i in range(p-1):
    if(c%2==0):
        print(c,end=" ")
        c=c+a[i+1]
    else:
        print(a[i],end=" ")
        c=c+a[i-1]
if(c%2==0):
    print(c)
else:
    print(a[p-1])