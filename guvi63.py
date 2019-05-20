x=list(map(int,input().split()))
for i in range(0,len(x)-2):
    for j in range(0,len(x)-2-i):
        if x[j] > x[j + 1]:
            k=x[j]
            x[j]=x[j+1]
            x[j+1]=k
print(x[0])
