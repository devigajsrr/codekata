o=int(input())
l=[]
for i in range(2,o+1):
    s=0
    if o%i==0:
        for j in range(2,i):
            if i%j==0:
                s=1
                break
        if s==0: l.append(i)
print(*l)