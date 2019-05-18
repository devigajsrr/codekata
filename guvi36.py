x=list(map(str,input()))
n=len(x)
c=0
for i in range(0,n):
   if x[i].isdigit()!=0 or x[i].isalpha()!=0:
       c=c+1
print(abs(n-c))