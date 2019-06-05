o,r=map(int,input().split())
q=o*r
m=[]
for i in range(1,q+1):
    if i%o==0 and i%r==0:
        m.append(i)
print(min(m))