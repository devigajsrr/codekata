x=list(map(str,input()))
n=len(x)
c=1
for i in range(0,n):
   if x[i]==".":
       c=c+1
print(c)