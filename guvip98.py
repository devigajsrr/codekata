m,k=map(str,input().split())
m=list(m)
k=int(k)
j=-1
for i in range(0,k+1):
    if str(i) in m: j=j+1
if j==k: print("yes")
else: print("no")
