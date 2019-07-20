def fac(m):
    k=1
    for i in range(1,m+1):
        k=k*i
    return k
m,k=map(int,input().split())
print(fac(m)//fac(k))