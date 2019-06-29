def fac(m):
    s=1
    for i in range(1,m+1):
        s=s*i
    return s
m,k=map(int,input().split())
print(fac(m)//(fac(m-k)*fac(k)))