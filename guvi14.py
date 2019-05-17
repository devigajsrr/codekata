    
m,n=input().split()
m=int(m)
n=int(n)
for i in range (m+1,n):
    if i % 2 != 0:
        print(i,end=" ")