x=int(input())
a=0
c=[]
while x>0:
    a=x%10
    c.append(a)
    x=x//10
for i in range(-1,-len(c)-1,-1):
    print(c[i],end=" ")